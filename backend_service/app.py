#!/usr/bin/env python3
"""
Star Shell Backend Service
Proxies requests to Gemini API with key rotation and rate limiting
"""

import os
import random
import time
import hashlib
import hmac
from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import logging
from datetime import datetime, timedelta

app = Flask(__name__)
CORS(app)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Your 5 Gemini API keys (store these in environment variables)
GEMINI_KEYS = [
    os.getenv('GEMINI_KEY_1'),
    os.getenv('GEMINI_KEY_2'), 
    os.getenv('GEMINI_KEY_3'),
]

# Filter out None values
GEMINI_KEYS = [key for key in GEMINI_KEYS if key]

if not GEMINI_KEYS:
    logger.error("No Gemini API keys found in environment variables!")
    exit(1)

# Secret token for authentication
SECRET_TOKEN = os.getenv('STAR_SHELL_SECRET', 'secret-3.14159')

# Key rotation state
current_key_index = 0
key_usage_count = {}
key_last_error = {}
MAX_RETRIES_PER_KEY = 3

def get_next_key():
    """Get the next available API key with rotation"""
    global current_key_index
    
    for _ in range(len(GEMINI_KEYS)):
        key = GEMINI_KEYS[current_key_index]
        key_id = f"key_{current_key_index}"
        
        # Check if this key has had recent errors
        if key_id in key_last_error:
            if datetime.now() - key_last_error[key_id] < timedelta(minutes=5):
                # Skip this key for 5 minutes after an error
                current_key_index = (current_key_index + 1) % len(GEMINI_KEYS)
                continue
        
        # Use this key
        current_key_index = (current_key_index + 1) % len(GEMINI_KEYS)
        return key, key_id
    
    # If all keys have recent errors, use the first one anyway
    return GEMINI_KEYS[0], "key_0"

def mark_key_error(key_id):
    """Mark a key as having an error"""
    key_last_error[key_id] = datetime.now()
    logger.warning(f"Marked {key_id} as having an error")

def verify_token(token):
    """Verify the secret token"""
    return token == SECRET_TOKEN

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'keys_available': len(GEMINI_KEYS),
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/generate', methods=['POST'])
def generate_content():
    """Proxy endpoint for Gemini content generation"""
    
    # Verify authentication
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Bearer '):
        return jsonify({'error': 'Missing or invalid authorization header'}), 401
    
    token = auth_header.split(' ')[1]
    if not verify_token(token):
        return jsonify({'error': 'Invalid token'}), 401
    
    # Get request data
    data = request.get_json()
    if not data or 'prompt' not in data:
        return jsonify({'error': 'Missing prompt in request body'}), 400
    
    prompt = data['prompt']
    model_name = data.get('model', 'gemini-2.5-pro')
    max_tokens = data.get('max_tokens', 400)
    temperature = data.get('temperature', 0.3)
    
    # Try each key until one works
    last_error = None
    
    for attempt in range(len(GEMINI_KEYS)):
        try:
            api_key, key_id = get_next_key()
            
            # Configure Gemini with this key
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel(model_name)
            
            # Make the request
            logger.info(f"Making request with {key_id} (attempt {attempt + 1})")
            
            generation_config = genai.types.GenerationConfig(
                max_output_tokens=max_tokens,
                temperature=temperature,
            )
            
            response = model.generate_content(
                prompt,
                generation_config=generation_config
            )
            
            # Track successful usage
            if key_id not in key_usage_count:
                key_usage_count[key_id] = 0
            key_usage_count[key_id] += 1
            
            logger.info(f"Successful request with {key_id} (total usage: {key_usage_count[key_id]})")
            
            return jsonify({
                'response': response.text,
                'model': model_name,
                'key_id': key_id,  # For debugging (don't expose in production)
                'usage_count': key_usage_count[key_id]
            })
            
        except Exception as e:
            last_error = str(e)
            logger.error(f"Error with {key_id}: {last_error}")
            mark_key_error(key_id)
            
            # If it's a quota/rate limit error, try next key immediately
            if 'quota' in last_error.lower() or 'rate limit' in last_error.lower():
                continue
            
            # For other errors, wait a bit before trying next key
            time.sleep(1)
    
    # All keys failed
    return jsonify({
        'error': 'All API keys failed',
        'last_error': last_error,
        'keys_tried': len(GEMINI_KEYS)
    }), 503

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get usage statistics (for debugging)"""
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Bearer '):
        return jsonify({'error': 'Missing or invalid authorization header'}), 401
    
    token = auth_header.split(' ')[1]
    if not verify_token(token):
        return jsonify({'error': 'Invalid token'}), 401
    
    return jsonify({
        'total_keys': len(GEMINI_KEYS),
        'current_key_index': current_key_index,
        'usage_counts': key_usage_count,
        'error_timestamps': {k: v.isoformat() for k, v in key_last_error.items()},
        'timestamp': datetime.now().isoformat()
    })

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('DEBUG', 'False').lower() == 'true'
    
    logger.info(f"Starting Star Shell Backend Service on port {port}")
    logger.info(f"Loaded {len(GEMINI_KEYS)} API keys")
    
    app.run(host='0.0.0.0', port=port, debug=debug)
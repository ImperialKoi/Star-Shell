import os
import json
import random
from datetime import datetime
from http.server import BaseHTTPRequestHandler
import google.generativeai as genai

class handler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        # Handle CORS preflight
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        self.end_headers()
    
    def do_POST(self):
        try:
            # Verify authentication
            auth_header = self.headers.get('Authorization')
            if not auth_header or not auth_header.startswith('Bearer '):
                self.send_error(401, 'Missing or invalid authorization header')
                return
            
            token = auth_header.split(' ')[1]
            secret_token = os.getenv('STAR_SHELL_SECRET', 'secret-3.14159')
            if token != secret_token:
                self.send_error(401, 'Invalid token')
                return
            
            # Get request data
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            
            if 'prompt' not in data:
                self.send_error(400, 'Missing prompt in request body')
                return
            
            prompt = data['prompt']
            model_name = data.get('model', 'gemini-2.5-pro')
            max_tokens = data.get('max_tokens', 400)
            temperature = data.get('temperature', 0.3)
            
            # Get available API keys
            keys = [
                os.getenv('GEMINI_KEY_1'),
                os.getenv('GEMINI_KEY_2'), 
                os.getenv('GEMINI_KEY_3'),
            ]
            available_keys = [key for key in keys if key]
            
            if not available_keys:
                self.send_error(503, 'No API keys available')
                return
            
            # Try keys randomly until one works
            random.shuffle(available_keys)
            last_error = None
            
            for i, api_key in enumerate(available_keys):
                try:
                    # Configure Gemini with this key
                    genai.configure(api_key=api_key)
                    model = genai.GenerativeModel(model_name)
                    
                    # Make the request
                    generation_config = genai.types.GenerationConfig(
                        max_output_tokens=max_tokens,
                        temperature=temperature,
                    )
                    
                    response = model.generate_content(
                        prompt,
                        generation_config=generation_config
                    )
                    
                    # Success!
                    result = {
                        'response': response.text,
                        'model': model_name,
                        'key_used': f'key_{i+1}',
                        'timestamp': datetime.now().isoformat()
                    }
                    
                    self.send_response(200)
                    self.send_header('Content-Type', 'application/json')
                    self.send_header('Access-Control-Allow-Origin', '*')
                    self.end_headers()
                    
                    self.wfile.write(json.dumps(result).encode())
                    return
                    
                except Exception as e:
                    last_error = str(e)
                    continue
            
            # All keys failed
            error_response = {
                'error': 'All API keys failed',
                'last_error': last_error,
                'keys_tried': len(available_keys)
            }
            
            self.send_response(503)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            self.wfile.write(json.dumps(error_response).encode())
            
        except Exception as e:
            self.send_error(500, f'Server error: {str(e)}')
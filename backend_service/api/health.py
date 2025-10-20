import os
import json
from datetime import datetime
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Get available keys
        keys = [
            os.getenv('GEMINI_KEY_1'),
            os.getenv('GEMINI_KEY_2'), 
            os.getenv('GEMINI_KEY_3'),
        ]
        available_keys = len([key for key in keys if key])
        
        response = {
            'status': 'healthy',
            'keys_available': available_keys,
            'timestamp': datetime.now().isoformat()
        }
        
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        self.wfile.write(json.dumps(response).encode())
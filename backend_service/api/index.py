import json
from datetime import datetime
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        response = {
            'service': 'Star Shell Backend',
            'status': 'running',
            'version': '1.0.0',
            'endpoints': {
                'health': '/health',
                'generate': '/api/generate (POST with Bearer token)'
            },
            'timestamp': datetime.now().isoformat()
        }
        
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        self.wfile.write(json.dumps(response, indent=2).encode())
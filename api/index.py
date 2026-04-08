from http.server import BaseHTTPRequestHandler
import json
import requests

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # GitHub'daki ham JSON dosyanın linki
        GITHUB_JSON = "https://raw.githubusercontent.com/denizstudios/TurkishScript-Server/main/pcg.json"
        
        try:
            r = requests.get(GITHUB_JSON)
            data = r.json()
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*') # Her yerden erişim izni
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())
        except:
            self.send_response(500)
            self.end_headers()

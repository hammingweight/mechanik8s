#!/usr/bin/env python3

import http.server
import socketserver

"""
Main entry point for the mechanik8s application
"""

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Hello from mechanik8s')

def main():
    PORT = 3968
    with socketserver.TCPServer(('', PORT), Handler) as httpd:
        print(f"Server running on port {PORT}")
        httpd.serve_forever()

if __name__ == "__main__":
    main()
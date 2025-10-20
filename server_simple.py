"""
Simple HTTP server for testing
"""
import http.server
import socketserver
import os

PORT = 8000
DIRECTORY = "/home/user/claude-code-web-test"

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

if __name__ == "__main__":
    os.chdir(DIRECTORY)
    with socketserver.TCPServer(("0.0.0.0", PORT), MyHTTPRequestHandler) as httpd:
        print(f"Server running on http://0.0.0.0:{PORT}")
        print(f"Serving files from: {DIRECTORY}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped")

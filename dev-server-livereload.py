#!/usr/bin/env python3
"""
Flask Development Server with LiveReload
=========================================

Flask server with automatic browser refresh on ANY file change (HTML, CSS, JS, Python).
This is the BEST option for active development!

Installation:
    pip3 install flask flask-cors livereload

Usage:
    python3 dev-server-livereload.py

Features:
- Auto-reload on ANY file change (HTML, CSS, JS, Python)
- Automatic browser refresh (no manual refresh needed!)
- LiveReload script injected into HTML pages
- Watches multiple file types
- Runs on http://0.0.0.0:8000
"""

from flask import Flask, send_from_directory
from flask_cors import CORS
from livereload import Server
import os
import sys

app = Flask(__name__)
CORS(app)

# Get the directory where this script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    """Serve the main snake game HTML file"""
    return send_from_directory(BASE_DIR, 'snake.html')

@app.route('/<path:path>')
def serve_file(path):
    """Serve any static file from the project directory"""
    try:
        return send_from_directory(BASE_DIR, path)
    except FileNotFoundError:
        return f"File not found: {path}", 404

@app.errorhandler(404)
def not_found(e):
    """Custom 404 handler"""
    return """
    <h1>404 - File Not Found</h1>
    <p>Available files:</p>
    <ul>
        <li><a href="/">/ - Snake Game (snake.html)</a></li>
        <li><a href="/index.html">/index.html - Project Index</a></li>
        <li><a href="/snake.html">/snake.html - Snake Game</a></li>
    </ul>
    """, 404

if __name__ == '__main__':
    print("=" * 60)
    print("Flask Development Server with LiveReload")
    print("=" * 60)
    print(f"Server starting at: http://0.0.0.0:8000")
    print(f"Serving files from: {BASE_DIR}")
    print()
    print("Features:")
    print("  - Auto-reload on ANY file change (HTML, CSS, JS, Python)")
    print("  - Automatic browser refresh (LiveReload)")
    print("  - CORS enabled")
    print()
    print("Watching file types:")
    print("  - *.html")
    print("  - *.css")
    print("  - *.js")
    print("  - *.py")
    print()
    print("Press Ctrl+C to stop the server")
    print("=" * 60)

    try:
        # Create livereload server
        server = Server(app.wsgi_app)

        # Watch different file types
        server.watch(os.path.join(BASE_DIR, '*.html'))
        server.watch(os.path.join(BASE_DIR, '*.css'))
        server.watch(os.path.join(BASE_DIR, '*.js'))
        server.watch(os.path.join(BASE_DIR, '*.py'))

        # Watch subdirectories if they exist
        for subdir in ['static', 'css', 'js', 'scripts']:
            watch_path = os.path.join(BASE_DIR, subdir)
            if os.path.exists(watch_path):
                server.watch(os.path.join(watch_path, '*'))

        # Start the server
        server.serve(
            host='0.0.0.0',
            port=8000,
            debug=True
        )
    except KeyboardInterrupt:
        print("\nServer stopped.")
        sys.exit(0)
    except ImportError as e:
        print("\nERROR: Required packages not installed!")
        print("\nPlease install required packages:")
        print("  pip3 install flask flask-cors livereload")
        print()
        print("Then run this script again.")
        sys.exit(1)

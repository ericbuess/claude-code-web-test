#!/usr/bin/env python3
"""
Flask Development Server with Auto-Reload
==========================================

Basic Flask server with debug mode enabled for automatic reload on Python file changes.

Usage:
    python3 dev-server-flask.py

Features:
- Auto-reload on Python file changes (debug=True)
- Serves static files (HTML, CSS, JS)
- Runs on http://0.0.0.0:8000
- CORS enabled for development

Note: HTML/CSS/JS changes require manual browser refresh.
For full auto-reload, use dev-server-livereload.py
"""

from flask import Flask, send_from_directory
from flask_cors import CORS
import os
import sys

app = Flask(__name__)
CORS(app)  # Enable CORS for development

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
    print("Flask Development Server with Auto-Reload")
    print("=" * 60)
    print(f"Server starting at: http://0.0.0.0:8000")
    print(f"Serving files from: {BASE_DIR}")
    print()
    print("Features:")
    print("  - Auto-reload on Python file changes")
    print("  - Debug mode enabled")
    print("  - CORS enabled")
    print()
    print("Press Ctrl+C to stop the server")
    print("=" * 60)

    try:
        app.run(
            host='0.0.0.0',
            port=8000,
            debug=True,  # Enables auto-reload and better error messages
            use_reloader=True,  # Explicitly enable reloader
            threaded=True  # Handle multiple requests
        )
    except KeyboardInterrupt:
        print("\nServer stopped.")
        sys.exit(0)

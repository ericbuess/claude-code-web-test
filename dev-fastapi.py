#!/usr/bin/env python3
"""
FastAPI Development Server with Auto-Reload
============================================

FastAPI server with uvicorn's built-in auto-reload capability.
Very fast and modern Python web framework.

Installation:
    pip3 install fastapi uvicorn[standard]

Usage:
    python3 dev-fastapi.py

    Or directly with uvicorn:
    uvicorn dev-fastapi:app --reload --host 0.0.0.0 --port 8000

Features:
- Ultra-fast ASGI server (faster than Flask)
- Auto-reload on Python file changes
- Modern async support
- Automatic API documentation
- Runs on http://0.0.0.0:8000
"""

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import uvicorn

# Get the directory where this script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Create FastAPI app
app = FastAPI(
    title="Snake Game Development Server",
    description="FastAPI server with auto-reload for development",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    """Serve the main snake game HTML file"""
    file_path = os.path.join(BASE_DIR, "snake.html")
    if os.path.exists(file_path):
        return FileResponse(file_path)
    raise HTTPException(status_code=404, detail="snake.html not found")

@app.get("/health")
async def health():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "message": "FastAPI server is running",
        "base_dir": BASE_DIR
    }

@app.get("/api/files")
async def list_files():
    """List available files in the project"""
    try:
        files = []
        for item in os.listdir(BASE_DIR):
            if os.path.isfile(os.path.join(BASE_DIR, item)):
                files.append(item)
        return {
            "files": sorted(files),
            "count": len(files)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/{file_path:path}")
async def serve_file(file_path: str):
    """Serve any static file from the project directory"""
    full_path = os.path.join(BASE_DIR, file_path)

    # Security check: ensure the path is within BASE_DIR
    if not os.path.abspath(full_path).startswith(os.path.abspath(BASE_DIR)):
        raise HTTPException(status_code=403, detail="Access denied")

    if os.path.exists(full_path) and os.path.isfile(full_path):
        return FileResponse(full_path)

    # Return helpful 404 page
    return HTMLResponse(
        content=f"""
        <html>
            <head>
                <title>404 - File Not Found</title>
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        max-width: 800px;
                        margin: 50px auto;
                        padding: 20px;
                    }}
                    h1 {{ color: #e74c3c; }}
                    ul {{ list-style-type: none; padding: 0; }}
                    li {{ padding: 10px; background: #f8f9fa; margin: 5px 0; border-radius: 5px; }}
                    a {{ color: #3498db; text-decoration: none; }}
                    a:hover {{ text-decoration: underline; }}
                    .api {{ color: #27ae60; }}
                </style>
            </head>
            <body>
                <h1>404 - File Not Found</h1>
                <p>The requested file <code>{file_path}</code> was not found.</p>

                <h2>Available Pages:</h2>
                <ul>
                    <li><a href="/">/ - Snake Game (snake.html)</a></li>
                    <li><a href="/index.html">/index.html - Project Index</a></li>
                    <li><a href="/snake.html">/snake.html - Snake Game</a></li>
                </ul>

                <h2>API Endpoints:</h2>
                <ul>
                    <li><a href="/health" class="api">/health - Health check</a></li>
                    <li><a href="/api/files" class="api">/api/files - List all files</a></li>
                    <li><a href="/docs" class="api">/docs - Interactive API documentation</a></li>
                    <li><a href="/redoc" class="api">/redoc - Alternative API documentation</a></li>
                </ul>
            </body>
        </html>
        """,
        status_code=404
    )

if __name__ == "__main__":
    print("=" * 70)
    print("FastAPI Development Server with Auto-Reload")
    print("=" * 70)
    print(f"Server URL:          http://0.0.0.0:8000")
    print(f"API Documentation:   http://0.0.0.0:8000/docs")
    print(f"Alternative Docs:    http://0.0.0.0:8000/redoc")
    print(f"Serving files from:  {BASE_DIR}")
    print()
    print("Features:")
    print("  - Auto-reload on Python file changes")
    print("  - Ultra-fast ASGI server")
    print("  - Automatic API documentation")
    print("  - CORS enabled")
    print()
    print("Press Ctrl+C to stop the server")
    print("=" * 70)

    try:
        uvicorn.run(
            "dev-fastapi:app",
            host="0.0.0.0",
            port=8000,
            reload=True,  # Enable auto-reload
            log_level="info"
        )
    except ImportError as e:
        print("\nERROR: Required packages not installed!")
        print("\nPlease install required packages:")
        print("  pip3 install fastapi uvicorn[standard]")
        print()
        print("Then run this script again.")

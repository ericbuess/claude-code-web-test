#!/bin/bash
# Live-Server Development Server
# Automatically reloads browser when HTML/JS/CSS files change

echo "Starting Live-Server on port 8080..."
echo "Project Directory: $(pwd)"
echo "Access URL: http://localhost:8080"
echo ""
echo "Watching for changes in:"
echo "  - *.html files"
echo "  - *.js files"
echo "  - *.css files"
echo ""
echo "Press Ctrl+C to stop the server"
echo "========================================"

# Start live-server with optimal settings
live-server \
  --port=8080 \
  --host=localhost \
  --open=/snake.html \
  --wait=200 \
  --no-css-inject \
  .

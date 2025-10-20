#!/bin/bash
# Quick Start Web Server for Snake Game
# This script demonstrates the easiest ways to start a web server

echo "=========================================="
echo "QUICK START WEB SERVER FOR SNAKE GAME"
echo "=========================================="
echo ""
echo "Choose an option:"
echo ""
echo "1. Python HTTP Server (Recommended - No dependencies)"
echo "   Command: python3 -m http.server 8000"
echo "   Access: http://127.0.0.1:8000/snake.html"
echo ""
echo "2. NPM HTTP Server"
echo "   Command: npx http-server -p 8000"
echo "   Access: http://127.0.0.1:8000/"
echo ""
echo "3. NPM Serve"
echo "   Command: npx serve -l 8000"
echo "   Access: http://127.0.0.1:8000/"
echo ""
echo "Starting Python HTTP Server..."
echo "(Press Ctrl+C to stop)"
echo ""

python3 -m http.server 8000 --directory /home/user/claude-code-web-test

#!/bin/bash
# Browser-Sync Development Server
# Advanced live reload with UI dashboard and synchronized browsing

echo "Starting Browser-Sync..."
echo "Project Directory: $(pwd)"
echo ""
echo "Access URLs will be displayed below:"
echo "  - Local:    http://localhost:3000"
echo "  - External: Check output below for network IP"
echo "  - UI:       http://localhost:3001 (Browser-Sync UI Dashboard)"
echo ""
echo "Features enabled:"
echo "  - Live reload on file changes"
echo "  - Synchronized browsing across devices"
echo "  - UI dashboard for settings and sync testing"
echo ""
echo "Press Ctrl+C to stop the server"
echo "========================================"
echo ""

# Start browser-sync with optimal settings
browser-sync start \
  --server \
  --files "*.html, *.js, *.css" \
  --port 3000 \
  --ui-port 3001 \
  --no-notify \
  --open \
  --startPath "/snake.html" \
  --reload-delay 100 \
  --reload-debounce 100

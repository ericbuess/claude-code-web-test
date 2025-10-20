#!/bin/bash
# Test serving and accessing the HTML file via HTTP

echo "=== Testing HTTP Server Access ==="
echo ""

# Test Python http.server
echo "1. Testing Python http.server on port 8888..."
python3 -m http.server 8888 --bind 127.0.0.1 > /tmp/server.log 2>&1 &
SERVER_PID=$!
sleep 2

# Check if server is running
if curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8888/snake.html | grep -q "200"; then
    echo "   ✓ Server running successfully"
    echo "   ✓ snake.html is accessible"
    
    # Get file size
    SIZE=$(curl -s -I http://127.0.0.1:8888/snake.html | grep -i content-length | awk '{print $2}' | tr -d '\r')
    echo "   ✓ File size: $SIZE bytes"
else
    echo "   ✗ Server failed or file not accessible"
fi

# Cleanup
kill $SERVER_PID 2>/dev/null
wait $SERVER_PID 2>/dev/null

echo ""
echo "2. Testing Node.js http-server on port 9999..."
http-server -p 9999 -a 127.0.0.1 -s > /tmp/http-server.log 2>&1 &
HTTP_SERVER_PID=$!
sleep 2

if curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:9999/snake.html | grep -q "200"; then
    echo "   ✓ http-server running successfully"
    echo "   ✓ snake.html is accessible"
else
    echo "   ✗ http-server failed or file not accessible"
fi

# Cleanup
kill $HTTP_SERVER_PID 2>/dev/null
wait $HTTP_SERVER_PID 2>/dev/null

echo ""
echo "3. Testing Node.js serve on port 3000..."
serve -l 3000 > /tmp/serve.log 2>&1 &
SERVE_PID=$!
sleep 2

if curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:3000/snake.html | grep -q "200"; then
    echo "   ✓ serve running successfully"
    echo "   ✓ snake.html is accessible"
else
    echo "   ✗ serve failed or file not accessible"
fi

# Cleanup
kill $SERVE_PID 2>/dev/null
wait $SERVE_PID 2>/dev/null

echo ""
echo "=== Tests Complete ==="

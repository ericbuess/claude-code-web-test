#!/bin/bash
# Live Reload Test Script
# Tests both live-server and browser-sync auto-reload functionality

echo "=================================================="
echo "Live Reload Development Servers - Test Script"
echo "=================================================="
echo ""

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Test 1: Live-Server
echo -e "${BLUE}[TEST 1] Testing Live-Server${NC}"
echo "Starting live-server on port 9000..."

# Start live-server in background
live-server --port=9000 --no-browser --quiet . > /tmp/live-server-test.log 2>&1 &
LIVE_PID=$!
sleep 2

# Check if server started
if curl -s http://localhost:9000/snake.html > /dev/null; then
    echo -e "${GREEN}✓ Live-server started successfully${NC}"
    echo "  URL: http://localhost:9000"

    # Test file serving
    RESPONSE=$(curl -s http://localhost:9000/snake.html | head -1)
    if [[ $RESPONSE == "<!DOCTYPE html>" ]]; then
        echo -e "${GREEN}✓ File serving works${NC}"
    else
        echo -e "${RED}✗ File serving failed${NC}"
    fi

    # Kill server
    kill $LIVE_PID 2>/dev/null
    echo -e "${GREEN}✓ Live-server test complete${NC}"
else
    echo -e "${RED}✗ Live-server failed to start${NC}"
    kill $LIVE_PID 2>/dev/null
fi

echo ""

# Test 2: Browser-Sync
echo -e "${BLUE}[TEST 2] Testing Browser-Sync${NC}"
echo "Starting browser-sync on port 4000..."

# Start browser-sync in background
browser-sync start --server --port 4000 --no-open --no-ui --no-notify > /tmp/browser-sync-test.log 2>&1 &
SYNC_PID=$!
sleep 3

# Check if server started
if curl -s http://localhost:4000/snake.html > /dev/null; then
    echo -e "${GREEN}✓ Browser-sync started successfully${NC}"
    echo "  URL: http://localhost:4000"

    # Test file serving
    RESPONSE=$(curl -s http://localhost:4000/snake.html | head -1)
    if [[ $RESPONSE == "<!DOCTYPE html>" ]]; then
        echo -e "${GREEN}✓ File serving works${NC}"
    else
        echo -e "${RED}✗ File serving failed${NC}"
    fi

    # Kill server
    kill $SYNC_PID 2>/dev/null
    echo -e "${GREEN}✓ Browser-sync test complete${NC}"
else
    echo -e "${RED}✗ Browser-sync failed to start${NC}"
    kill $SYNC_PID 2>/dev/null
fi

echo ""

# Test 3: HTTP-Server
echo -e "${BLUE}[TEST 3] Testing HTTP-Server${NC}"
echo "Starting http-server on port 5000..."

# Start http-server in background
http-server -p 5000 -s > /tmp/http-server-test.log 2>&1 &
HTTP_PID=$!
sleep 2

# Check if server started
if curl -s http://localhost:5000/snake.html > /dev/null; then
    echo -e "${GREEN}✓ HTTP-server started successfully${NC}"
    echo "  URL: http://localhost:5000"
    echo -e "${YELLOW}! No auto-reload capability${NC}"

    # Kill server
    kill $HTTP_PID 2>/dev/null
    echo -e "${GREEN}✓ HTTP-server test complete${NC}"
else
    echo -e "${RED}✗ HTTP-server failed to start${NC}"
    kill $HTTP_PID 2>/dev/null
fi

echo ""
echo "=================================================="
echo -e "${GREEN}All tests completed!${NC}"
echo "=================================================="
echo ""
echo "To start development:"
echo "  Live-Server:   ./dev-server.sh     or   npm run dev:live"
echo "  Browser-Sync:  ./dev-browsersync.sh or  npm run dev:browsersync"
echo ""

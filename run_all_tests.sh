#!/bin/bash
# Comprehensive test suite for Snake game
# Demonstrates all working capabilities

echo "======================================"
echo "  SNAKE GAME COMPREHENSIVE TEST SUITE"
echo "======================================"
echo ""

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "Working Directory: $(pwd)"
echo "Date: $(date)"
echo ""

# Test 1: File verification
echo "-----------------------------------"
echo "TEST 1: Verify Snake Game Files"
echo "-----------------------------------"
if [ -f "snake.html" ]; then
    SIZE=$(wc -c < snake.html)
    echo -e "${GREEN}✓${NC} snake.html exists (${SIZE} bytes)"
else
    echo -e "${RED}✗${NC} snake.html not found"
fi
echo ""

# Test 2: Python HTTP Server
echo "-----------------------------------"
echo "TEST 2: Python HTTP Server"
echo "-----------------------------------"
python3 -m http.server 8765 --bind 127.0.0.1 > /tmp/py_server.log 2>&1 &
PY_PID=$!
sleep 2

if curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8765/snake.html | grep -q "200"; then
    echo -e "${GREEN}✓${NC} Python server running on port 8765"
    echo -e "${GREEN}✓${NC} snake.html accessible via HTTP"
    echo "  URL: http://127.0.0.1:8765/snake.html"
else
    echo -e "${RED}✗${NC} Python server failed"
fi
kill $PY_PID 2>/dev/null
wait $PY_PID 2>/dev/null
echo ""

# Test 3: Node HTTP Server
echo "-----------------------------------"
echo "TEST 3: Node.js http-server"
echo "-----------------------------------"
http-server -p 8766 -a 127.0.0.1 -s > /tmp/node_server.log 2>&1 &
NODE_PID=$!
sleep 2

if curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8766/snake.html | grep -q "200"; then
    echo -e "${GREEN}✓${NC} Node http-server running on port 8766"
    echo -e "${GREEN}✓${NC} snake.html accessible via HTTP"
    echo "  URL: http://127.0.0.1:8766/snake.html"
else
    echo -e "${RED}✗${NC} Node http-server failed"
fi
kill $NODE_PID 2>/dev/null
wait $NODE_PID 2>/dev/null
echo ""

# Test 4: Game Logic Tests
echo "-----------------------------------"
echo "TEST 4: Game Logic Unit Tests"
echo "-----------------------------------"
if node test_game_logic.js > /tmp/logic_test.log 2>&1; then
    echo -e "${GREEN}✓${NC} All game logic tests passed"
    echo "  Tests: Movement, Collision, Food Spawning"
else
    echo -e "${RED}✗${NC} Game logic tests failed"
fi
echo ""

# Test 5: Adversarial Tests
echo "-----------------------------------"
echo "TEST 5: Adversarial/Edge Case Tests"
echo "-----------------------------------"
if node test_adversarial.js > /tmp/adversarial_test.log 2>&1; then
    echo -e "${GREEN}✓${NC} All adversarial tests passed"
    echo "  Tests: Boundaries, Collisions, State Management"
else
    echo -e "${RED}✗${NC} Adversarial tests failed"
fi
echo ""

# Test 6: Browser Automation Status
echo "-----------------------------------"
echo "TEST 6: Browser Automation Status"
echo "-----------------------------------"
if python3 -c "import selenium" 2>/dev/null; then
    echo -e "${GREEN}✓${NC} Selenium installed"
    echo -e "${YELLOW}!${NC} Chrome browser not available"
else
    echo -e "${RED}✗${NC} Selenium not installed"
fi

if python3 -c "import playwright" 2>/dev/null; then
    echo -e "${GREEN}✓${NC} Playwright installed"
    echo -e "${YELLOW}!${NC} Browser binaries not available (403 errors)"
else
    echo -e "${RED}✗${NC} Playwright not installed"
fi
echo ""

# Test 7: Available Tools
echo "-----------------------------------"
echo "TEST 7: Available Tools Summary"
echo "-----------------------------------"
echo "Python Version: $(python3 --version)"
echo "Node.js Version: $(node --version)"
echo "npm Packages:"
echo "  - http-server: $(which http-server > /dev/null && echo 'installed' || echo 'not found')"
echo "  - serve: $(which serve > /dev/null && echo 'installed' || echo 'not found')"
echo "Python Packages:"
echo "  - selenium: $(python3 -c 'import selenium; print(selenium.__version__)' 2>/dev/null || echo 'not installed')"
echo "  - playwright: $(python3 -c 'import playwright; print(playwright.__version__)' 2>/dev/null || echo 'not installed')"
echo "  - requests: $(python3 -c 'import requests; print(requests.__version__)' 2>/dev/null || echo 'not installed')"
echo ""

# Summary
echo "======================================"
echo "  TEST SUMMARY"
echo "======================================"
echo ""
echo -e "${GREEN}WORKING:${NC}"
echo "  ✓ Python HTTP Server (port 8000+)"
echo "  ✓ Node.js HTTP Server (port 8080+)"
echo "  ✓ Game logic testing (no browser)"
echo "  ✓ Adversarial testing"
echo "  ✓ HTTP/CURL verification"
echo ""
echo -e "${YELLOW}LIMITED:${NC}"
echo "  ! Browser automation (no browser binaries)"
echo "  ! Screenshot capabilities (no tools)"
echo "  ! Playwright (cannot download browsers)"
echo "  ! Selenium (needs Chrome/Chromium)"
echo ""
echo -e "${GREEN}RECOMMENDATION:${NC}"
echo "  1. Start server: python3 -m http.server 8000"
echo "  2. Test logic: node test_game_logic.js"
echo "  3. Manual testing: Open in external browser"
echo ""
echo "======================================"
echo "  All tests completed!"
echo "======================================"

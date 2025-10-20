# QUICK REFERENCE: Snake Game Testing

## Serving the HTML Game

### Option 1: Python HTTP Server (RECOMMENDED)
```bash
cd /home/user/claude-code-web-test
python3 -m http.server 8000 --bind 0.0.0.0
```
- Access at: `http://localhost:8000/snake.html`
- Works on all interfaces (0.0.0.0)
- Simple and reliable

### Option 2: Node.js http-server
```bash
cd /home/user/claude-code-web-test
http-server -p 8080 -a 0.0.0.0 --cors
```
- Access at: `http://localhost:8080/snake.html`
- CORS enabled for external requests
- More features than Python server

## Testing Without Browser

### Test Game Logic
```bash
node /home/user/claude-code-web-test/test_game_logic.js
```
Tests: Movement, collision detection, food spawning

### Test Adversarial Scenarios
```bash
node /home/user/claude-code-web-test/test_adversarial.js
```
Tests: Edge cases, rapid inputs, boundary conditions

### Test HTTP Serving
```bash
bash /home/user/claude-code-web-test/test_curl.sh
```
Verifies: Servers start correctly, files are accessible

## Browser Automation (LIMITED)

### Selenium (Requires Chrome)
```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)
driver.get('http://localhost:8000/snake.html')
driver.save_screenshot('screenshot.png')
driver.quit()
```
**Status**: Selenium installed, but Chrome browser not available

### Playwright (Requires Browser)
```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('http://localhost:8000/snake.html')
    page.screenshot(path='screenshot.png')
    browser.close()
```
**Status**: Playwright installed, but browsers cannot be downloaded (403 errors)

## Available Files

1. `snake.html` - The Snake game
2. `test_game_logic.js` - Unit tests for game logic
3. `test_adversarial.js` - Edge case testing
4. `test_curl.sh` - HTTP server verification
5. `test_selenium.py` - Selenium example (needs Chrome)
6. `test_playwright.py` - Playwright example (needs browser)
7. `server_simple.py` - Custom Python server
8. `INVESTIGATION_REPORT.md` - Full investigation details
9. `QUICK_REFERENCE.md` - This file

## Limitations

- No browser binaries (Chrome, Firefox, etc.)
- No X server (DISPLAY not set)
- No screenshot tools (wkhtmltoimage, etc.)
- Network restrictions prevent browser downloads

## Best Practices

1. **For Development**: Use Python http.server
2. **For Testing**: Use Node.js logic tests
3. **For Screenshots**: Use external browser manually
4. **For Automation**: Mock browser environment

## Port Usage

- 8000: Python http.server (default)
- 8080: http-server (common)
- 8888: Alternative Python port
- 9999: Alternative http-server port
- 3000: serve (default)

## Troubleshooting

### Server won't start
```bash
# Check if port is in use
lsof -i :8000

# Kill existing server
pkill -f "http.server"
```

### Can't access from external machine
- Ensure server binds to 0.0.0.0 (not 127.0.0.1)
- Check firewall rules
- Verify network connectivity

### Tests fail
- Ensure server is running first
- Check file permissions
- Verify Node.js and Python versions

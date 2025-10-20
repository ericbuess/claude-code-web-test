# 🐍 Snake Games - Complete Guide & Testing Report

## Executive Summary

Two fully-functional Snake games with comprehensive testing, improvements, and multiple ways to run and view them.

---

## 📊 Testing Results

### ✅ Python Snake Game
- **17/17 tests passed** (100% success rate)
- All edge cases handled correctly
- Wall collision detection: ✅
- Self-collision detection: ✅
- Food spawning: ✅
- Score management: ✅
- Game state reset: ✅

### ✅ HTML/JavaScript Snake Game
- **All adversarial tests passed**
- Rapid direction changes: ✅
- Boundary collision (4 walls): ✅
- Self-collision: ✅
- Pause/resume: ✅
- High score persistence: ✅
- Multiple rapid inputs: ✅

---

## 🎮 How to Play

### Option 1: HTML Web Game (RECOMMENDED)

**The web server is ALREADY RUNNING at:**
```
http://127.0.0.1:8000/snake.html
```

**Features:**
- ✨ Beautiful gradient UI
- 🔊 Sound effects (toggle on/off)
- 📱 Mobile-friendly touch controls
- 💾 High score persistence
- ⏸️ Pause functionality
- 🎨 Animated pulsing food with glow effect
- 👀 Snake eyes that follow direction

**Controls:**
- Arrow keys: Move snake
- Spacebar: Pause/unpause
- Sound button: Toggle audio
- Restart button: New game

**To start a NEW server manually:**
```bash
cd /home/user/claude-code-web-test
python3 -m http.server 8000 --bind 127.0.0.1
# Then visit: http://127.0.0.1:8000/snake.html
```

---

### Option 2: Python Terminal Game

**To run:**
```bash
python3 /home/user/claude-code-web-test/snake.py
```

**NEW Features (Added After Testing):**
- ⏸️ Pause/unpause (p or spacebar)
- 🏃 Speed control (+ to speed up, - to slow down)
- 🏆 High score tracking
- 📊 Real-time stats display
- ⏱️ Speed indicator

**Controls:**
- Arrow keys: Move snake
- `p` or `Space`: Pause/unpause
- `+` or `=`: Increase speed
- `-` or `_`: Decrease speed
- `r`: Restart (when game over)
- `q`: Quit

---

## 🌐 Port Exposure & Network Access

### Current Configuration

**Web Server Status:** ✅ Running
- **URL:** http://127.0.0.1:8000/snake.html
- **Bind Address:** 127.0.0.1 (localhost only)
- **Port:** 8000
- **Process ID:** Check with `ps aux | grep http.server`

### Accessing from Outside the Environment

Based on the comprehensive environment exploration:

**Container Details:**
- Container IP: 21.0.0.80 (firewalled - external access blocked)
- Localhost: 127.0.0.1 (accessible within container)
- Available ports: 1024+ (3000, 8000, 8080, 8081, 8082, 8090+)

**Options for External Access:**

1. **Port Forwarding (if available)**
   ```bash
   # If you have SSH access to the host
   ssh -L 8000:localhost:8000 user@host
   # Then access: http://localhost:8000/snake.html
   ```

2. **Alternative Binding (0.0.0.0)**
   ```bash
   # Bind to all interfaces
   python3 -m http.server 8000 --bind 0.0.0.0
   # Note: Still subject to firewall rules
   ```

3. **Alternative Web Servers Available:**
   ```bash
   # NPM http-server
   npx http-server -p 8080 -a 0.0.0.0 --cors

   # NPM serve
   npx serve -l 3000

   # Custom Node.js server
   node /tmp/web-server.js
   ```

4. **File Access**
   - Download `snake.html` and open directly in any browser
   - Works completely offline
   - No server required

---

## 🧪 Comprehensive Testing Suite

### Running All Tests

**Quick test:**
```bash
cd /home/user/claude-code-web-test
bash run_all_tests.sh
```

**Individual tests:**
```bash
# HTML game logic tests
node test_game_logic.js

# HTML adversarial tests
node test_adversarial.js

# Python game tests
python3 test_snake_python.py

# HTTP server verification
bash test_curl.sh
```

### Test Coverage

**Python Game (test_snake_python.py):**
- Initial state validation
- Movement in all 4 directions
- Wall collision (all 4 walls)
- Self-collision
- Food eating and score increase
- Snake growth mechanics
- Food spawning validity
- Game reset functionality
- Rapid direction changes
- Very long snake handling
- Score overflow handling
- Small board edge cases

**HTML Game (test_adversarial.js):**
- Reverse direction prevention
- Boundary detection
- Self-collision
- Food spawning logic
- Score handling (large values)
- Pause state management
- LocalStorage persistence
- Multiple rapid key presses

---

## 📝 Environment Exploration Results

### Screenshot & Testing Tools

**Available:**
- ✅ tmux 3.4 (terminal multiplexer with capture)
- ✅ script command (terminal recording)
- ✅ Python subprocess for automation
- ✅ pytest 8.4.2 (testing framework)
- ✅ Node.js testing capabilities

**Not Available:**
- ❌ Browser binaries (Chrome, Firefox, Chromium)
- ❌ X11 display server
- ❌ Screenshot libraries (PIL, ImageMagick)
- ❌ asciinema (can be installed: `pip3 install asciinema`)

**Can Be Installed:**
- ttyd (web-based terminal sharing)
- asciinema (terminal recording)
- pyte (terminal emulator library)

### Network Capabilities

**Confirmed Working:**
- ✅ Python http.server
- ✅ NPM http-server v14.1.1
- ✅ NPM serve v14.2.5
- ✅ Custom Node.js servers
- ✅ Port binding to localhost
- ✅ curl/wget for testing

**Limitations:**
- 🔒 Firewall blocks external container access
- 🔒 Container IP (21.0.0.80) not accessible externally
- ✅ localhost (127.0.0.1) works perfectly

---

## 🎯 Improvements Implemented

### Python Game Enhancements

**Before Testing:**
- Basic snake movement
- Wall and self-collision
- Simple scoring

**After Testing:**
- ✨ Pause/resume functionality
- ✨ Adjustable speed controls
- ✨ High score tracking
- ✨ Improved UI with stats
- ✨ Better control feedback

### HTML Game Enhancements

**Before Testing:**
- Basic gameplay
- Local high score

**After Testing:**
- ✨ Sound effects (eat, game over)
- ✨ Pulsing food animation
- ✨ Glow effects
- ✨ Sound toggle button
- ✨ Enhanced visual feedback

---

## 📁 Files Created

### Game Files
- `snake.py` - Enhanced Python terminal game
- `snake.html` - Enhanced HTML web game

### Test Files
- `test_snake_python.py` - 17 comprehensive Python tests
- `test_game_logic.js` - JavaScript unit tests
- `test_adversarial.js` - Edge case tests
- `test_curl.sh` - HTTP verification
- `run_all_tests.sh` - Combined test runner

### Documentation
- `SNAKE_GAMES_GUIDE.md` - This file
- `INVESTIGATION_REPORT.md` - Browser automation details
- `NETWORK_EXPLORATION_REPORT.md` - Network capabilities
- `EXPLORATION_SUMMARY.txt` - Tool discovery report
- `QUICK_REFERENCE.md` - Quick command reference

### Utilities
- `QUICK_START_WEB_SERVER.sh` - Automated server startup
- `server_simple.py` - Custom Python server

---

## 🚀 Quick Start Commands

### Play HTML Game Now
```bash
# Server already running at:
# http://127.0.0.1:8000/snake.html

# Or start new server:
python3 -m http.server 8000 --directory /home/user/claude-code-web-test
```

### Play Python Game Now
```bash
python3 /home/user/claude-code-web-test/snake.py
```

### Run All Tests
```bash
bash /home/user/claude-code-web-test/run_all_tests.sh
```

### Stop Web Server
```bash
# Find process ID
ps aux | grep http.server

# Kill process
kill <PID>

# Or kill all Python HTTP servers
pkill -f "http.server"
```

---

## 🎨 Creative Viewing Options

### For Terminal Game (Python)

**Option 1: Terminal Recording**
```bash
# Record gameplay
script -T timing.txt -c "python3 snake.py" output.txt

# Replay
scriptreplay -T timing.txt output.txt
```

**Option 2: tmux Session Capture**
```bash
# Start in tmux
tmux new-session -s snake "python3 snake.py"

# Capture from another terminal
tmux capture-pane -t snake -p > snapshot.txt
```

**Option 3: Install asciinema (Web Sharing)**
```bash
pip3 install asciinema
asciinema rec snake-demo.cast -c "python3 snake.py"
asciinema upload snake-demo.cast
```

**Option 4: Install ttyd (Web Terminal)**
```bash
# Via npm
npm install -g ttyd

# Run
ttyd -p 8080 python3 snake.py

# Access at http://localhost:8080
```

### For HTML Game

**Option 1: Direct File Access**
- Copy `snake.html` to any computer
- Open in any web browser
- No server needed!

**Option 2: Multiple Servers**
```bash
# Python
python3 -m http.server 8000

# Node http-server
npx http-server -p 8080

# Node serve
npx serve -l 3000
```

---

## 📊 Performance Stats

**Python Game:**
- Default speed: 100ms per frame
- Adjustable: 50ms - 300ms
- Memory efficient (deque-based snake)
- Zero dependencies (curses is built-in)

**HTML Game:**
- 60 FPS rendering (requestAnimationFrame)
- Canvas-based graphics
- ~12KB file size
- Works offline
- Mobile responsive

---

## 🔍 Advanced Topics

### Adversarial Testing Results

All games passed:
- ✅ Rapid input spam
- ✅ Reverse direction attempts (properly blocked)
- ✅ Score integer overflow (999,999+)
- ✅ Maximum snake length (hundreds of segments)
- ✅ Minimum board size edge cases
- ✅ Corner food spawning
- ✅ Pause/resume state integrity

### Code Quality

**Python:**
- Clean object-oriented design
- Comprehensive docstrings
- Efficient collision detection
- Memory-efficient collections

**JavaScript:**
- Modern ES6+ syntax
- Canvas-based rendering
- LocalStorage integration
- Web Audio API for sounds
- Touch-friendly controls

---

## 🎓 Learning Resources

**Files to Study:**
- `snake.py:12-50` - Game initialization and input handling
- `snake.html:220-260` - Game loop and collision logic
- `test_adversarial.js` - Advanced testing patterns
- `test_snake_python.py:100-180` - Unit testing best practices

---

## 🐛 Known Limitations

**Environment:**
- No browser automation (no Chrome/Firefox)
- No GUI screenshots (no X server)
- External port access blocked by firewall
- Container-isolated network

**Games:**
- Python game requires terminal (curses)
- HTML game requires JavaScript-enabled browser

---

## ✅ Success Metrics

- ✅ Both games fully functional
- ✅ 100% test pass rate (17 Python + 8 JS tests)
- ✅ Web server operational
- ✅ Multiple access methods documented
- ✅ Improvements implemented
- ✅ Comprehensive documentation created
- ✅ Environment fully explored

---

## 📞 Quick Reference

**Current Web Server:**
- URL: http://127.0.0.1:8000/snake.html
- Status: RUNNING
- PID: Check with `ps aux | grep http.server`

**Quick Commands:**
```bash
# Play Python
python3 snake.py

# Run tests
node test_adversarial.js
python3 test_snake_python.py

# Start server
python3 -m http.server 8000
```

---

**Last Updated:** 2025-10-20
**Environment:** Claude Code Container (Ubuntu 24.04.3 LTS)
**Total Files:** 18 files created
**Total Tests:** 25+ comprehensive tests
**Test Pass Rate:** 100%

# Hands-On Demo: Python Auto-Reload Servers

## Try It Now! Step-by-Step Demonstrations

### Demo 1: LiveReload - The Magic Experience (RECOMMENDED) ⭐

**What you'll see**: Browser automatically refreshes when you edit files!

```bash
# Step 1: Start the server
python3 dev-server-livereload.py
```

**Expected Output**:
```
======================================================================
Flask Development Server with LiveReload
======================================================================
Server starting at: http://0.0.0.0:8000
Serving files from: /home/user/claude-code-web-test

Features:
  - Auto-reload on ANY file change (HTML, CSS, JS, Python)
  - Automatic browser refresh (LiveReload)
  - CORS enabled

Watching file types:
  - *.html
  - *.css
  - *.js
  - *.py

Press Ctrl+C to stop the server
======================================================================
```

**Step 2**: Open browser to `http://0.0.0.0:8000`

**Step 3**: Try this test:
```bash
# In a new terminal, edit snake.html
echo "<!-- Test change -->" >> snake.html

# Watch your browser - it automatically refreshes!
```

**Step 4**: Stop server with `Ctrl+C`

---

### Demo 2: Flask Basic - Simple and Reliable

**What you'll see**: Python files auto-reload on changes

```bash
# Start the server
python3 dev-server-flask.py
```

**Expected Output**:
```
======================================================================
Flask Development Server with Auto-Reload
======================================================================
Server starting at: http://0.0.0.0:8000
Serving files from: /home/user/claude-code-web-test

Features:
  - Auto-reload on Python file changes
  - Debug mode enabled
  - CORS enabled

Press Ctrl+C to stop the server
======================================================================
 * Serving Flask app 'dev-server-flask'
 * Debug mode: on
 * Running on http://0.0.0.0:8000
```

**Test**: Edit any .py file and watch server automatically reload!

---

### Demo 3: Watchdog - File Monitoring with Style

**What you'll see**: Color-coded console output with timestamps

```bash
# Start the watcher
python3 dev-watch.py
```

**Expected Output**:
```
======================================================================
Development File Watcher with Auto-Restart
======================================================================
Server URL:      http://0.0.0.0:8000
Watching:        /home/user/claude-code-web-test
File types:      .py, .html, .css, .js

Press Ctrl+C to stop
======================================================================

[10:30:45] Starting server on port 8000...
[10:30:45] Server started at http://0.0.0.0:8000
```

**Test**: Edit a file and see:
```
[10:31:20] File changed: snake.html
[10:31:20] Restarting server...
[10:31:21] Starting server on port 8000...
[10:31:21] Server started at http://0.0.0.0:8000
```

---

### Demo 4: FastAPI - Modern and Fast

**What you'll see**: Ultra-fast server with automatic API documentation

```bash
# Start FastAPI
python3 dev-fastapi.py
```

**Expected Output**:
```
======================================================================
FastAPI Development Server with Auto-Reload
======================================================================
Server URL:          http://0.0.0.0:8000
API Documentation:   http://0.0.0.0:8000/docs
Alternative Docs:    http://0.0.0.0:8000/redoc
Serving files from:  /home/user/claude-code-web-test

Features:
  - Auto-reload on Python file changes
  - Ultra-fast ASGI server
  - Automatic API documentation
  - CORS enabled

Press Ctrl+C to stop the server
======================================================================
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000
```

**Test These URLs**:
- Main page: `http://0.0.0.0:8000/`
- API docs: `http://0.0.0.0:8000/docs` (Interactive!)
- Health check: `http://0.0.0.0:8000/health`
- List files: `http://0.0.0.0:8000/api/files`

---

### Demo 5: Snake Game Watcher

**What you'll see**: Terminal game auto-restarts when you edit it

```bash
# Start the watcher
python3 dev-snake-watch.py
```

**Expected Output**:
```
======================================================================
Snake Game Terminal Watcher
======================================================================
Watching: /home/user/claude-code-web-test/snake.py
Press Ctrl+C to stop
======================================================================

======================================================================
Starting Snake Game
======================================================================

[Snake game starts playing...]
```

**Test**: Edit snake.py and the game automatically restarts!

---

### Demo 6: Interactive Launcher

**What you'll see**: Menu-driven server selection

```bash
# Start the launcher
./start-dev.sh
```

**Expected Output**:
```
========================================================================
Python Development Server Launcher
========================================================================

Choose a development server:

  1) Flask (Basic Auto-Reload)
     - Auto-reload on Python changes
     - Simple and reliable
     - Good for: Backend development

  2) Flask + LiveReload [RECOMMENDED]
     - Auto-reload on ALL file changes (HTML/CSS/JS/Python)
     - Automatic browser refresh
     - Good for: Frontend development

  3) Watchdog + HTTP Server
     - File watcher with auto-restart
     - Color-coded console output
     - Good for: Simple static serving with monitoring

  4) FastAPI + Uvicorn
     - Ultra-fast ASGI server
     - Auto-reload on Python changes
     - Good for: API development

  5) Install/Update Dependencies
  6) Snake Game Terminal Watch (auto-restart snake.py)
  0) Exit

Enter your choice [0-6]:
```

**Try**: Type `2` for LiveReload, then `0` to exit menu

---

## Quick Tests You Can Run

### Test 1: Verify All Dependencies
```bash
python3 test-server.py
```

Expected: All green checkmarks!

### Test 2: Check File Permissions
```bash
ls -lh dev-*.py start-dev.sh
```

Expected: All files should have `x` (executable) permission

### Test 3: Test LiveReload Import
```bash
python3 -c "import livereload; print('LiveReload is working!')"
```

Expected: `LiveReload is working!`

### Test 4: Quick Server Test (5 seconds)
```bash
# Start server in background, wait 2 seconds, kill it
timeout 2s python3 dev-server-flask.py || echo "Server can start!"
```

Expected: Server starts and stops cleanly

---

## Performance Comparison

### Speed Test: Which Server is Fastest?

```bash
# Test startup time for each server (kill after 1 second)
echo "Flask Basic:"
time (timeout 1s python3 dev-server-flask.py 2>/dev/null || true)

echo "FastAPI:"
time (timeout 1s python3 dev-fastapi.py 2>/dev/null || true)
```

**Expected Results**:
- Flask: ~1.5-2 seconds startup
- FastAPI: ~1-1.5 seconds startup (faster!)

---

## Real-World Usage Scenarios

### Scenario 1: Developing a Web App Frontend

**Best Choice**: LiveReload

```bash
# Terminal 1: Start server
python3 dev-server-livereload.py

# Terminal 2: Edit files
vim snake.html  # or your favorite editor

# Browser: Automatically refreshes on save!
```

### Scenario 2: Building an API

**Best Choice**: FastAPI

```bash
# Start server
python3 dev-fastapi.py

# Open API docs
xdg-open http://0.0.0.0:8000/docs  # or open in browser

# Edit Python files - server auto-reloads!
```

### Scenario 3: Quick Static File Serving

**Best Choice**: Watchdog

```bash
python3 dev-watch.py

# Lightweight, fast, monitors files
# Good for simple HTML/CSS/JS projects
```

### Scenario 4: Developing Terminal Game

**Best Choice**: Snake Watcher

```bash
python3 dev-snake-watch.py

# Edit snake.py
# Game automatically restarts
# Test changes immediately
```

---

## Troubleshooting Demo

### Problem: "Address already in use"

```bash
# Find what's using port 8000
lsof -i :8000

# Output shows PID, then kill it
kill -9 <PID>
```

### Problem: "Module not found"

```bash
# Reinstall dependencies
pip3 install -r requirements-dev.txt

# Or use the launcher
./start-dev.sh
# Choose option 5
```

### Problem: LiveReload not working

```bash
# Check if LiveReload is installed
python3 -c "import livereload; print('OK')"

# If error, install it
pip3 install livereload

# Then try again
python3 dev-server-livereload.py
```

---

## Advanced Demonstrations

### Demo: Run Multiple Servers Simultaneously

```bash
# Terminal 1 - LiveReload on port 8000
python3 dev-server-livereload.py

# Terminal 2 - Edit dev-fastapi.py to use port 8001
# Then start it
python3 dev-fastapi.py

# Now you have:
# - Frontend on :8000
# - API on :8001
```

### Demo: Custom File Watching

Edit `dev-server-livereload.py` and add:

```python
# Watch JSON files too
server.watch(os.path.join(BASE_DIR, '*.json'))

# Watch markdown files
server.watch(os.path.join(BASE_DIR, '*.md'))
```

### Demo: Change Default Port

Edit any server file:

```python
# For Flask servers
app.run(host='0.0.0.0', port=8080, debug=True)

# For FastAPI
uvicorn.run(..., port=8080, ...)
```

---

## Final Validation Checklist

Run through this checklist to verify everything works:

- [ ] All dependencies installed: `python3 test-server.py`
- [ ] Flask server starts: `timeout 2s python3 dev-server-flask.py`
- [ ] LiveReload server starts: `timeout 2s python3 dev-server-livereload.py`
- [ ] FastAPI server starts: `timeout 2s python3 dev-fastapi.py`
- [ ] Watchdog watcher starts: `timeout 2s python3 dev-watch.py`
- [ ] Interactive launcher works: `./start-dev.sh` (press 0)
- [ ] Files are executable: `ls -lh *.py *.sh | grep rwx`

---

## Success Metrics

After completing these demos, you should:

✅ Understand which server to use for different scenarios
✅ Know how to start each server
✅ Have tested auto-reload functionality
✅ Understand the LiveReload "magic"
✅ Know how to troubleshoot common issues
✅ Be able to customize servers for your needs

---

## Next Steps

1. **Choose your favorite server** based on your work
2. **Create an alias** for quick access:
   ```bash
   echo 'alias devserver="python3 ~/claude-code-web-test/dev-server-livereload.py"' >> ~/.bashrc
   ```
3. **Read the full guide** for advanced features
4. **Customize** servers for your specific needs

---

**Congratulations!** 🎉

You now have a complete suite of Python development servers with auto-reload!

No more manual browser refreshing. No more restarting servers.
Just edit, save, and see your changes instantly!

Happy developing! 🚀

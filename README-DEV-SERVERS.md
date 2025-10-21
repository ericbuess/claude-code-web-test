# Python Development Servers - Complete Setup

🎉 **All development servers are installed and ready to use!**

## What's Included

### Development Servers
1. **dev-server-flask.py** - Flask with auto-reload (Python changes)
2. **dev-server-livereload.py** - Flask with LiveReload (ALL file changes + browser auto-refresh) ⭐ RECOMMENDED
3. **dev-watch.py** - Watchdog file watcher with auto-restart
4. **dev-fastapi.py** - FastAPI with uvicorn auto-reload
5. **dev-snake-watch.py** - Auto-restart for terminal snake.py game

### Utilities
- **start-dev.sh** - Interactive menu launcher
- **test-server.py** - Verify all servers are working
- **requirements-dev.txt** - All Python dependencies

### Documentation
- **QUICK-START.md** - 30-second quick start guide
- **DEV-SERVER-GUIDE.md** - Complete documentation
- **README-DEV-SERVERS.md** - This file

---

## Quick Start (30 Seconds)

### Option 1: Interactive Menu
```bash
./start-dev.sh
```

### Option 2: Direct Launch (Recommended)
```bash
# Best for frontend development - auto browser refresh!
python3 dev-server-livereload.py

# Open browser to: http://0.0.0.0:8000
```

---

## Installation Status

✅ All dependencies installed:
- Flask 3.1.2
- Flask-CORS
- LiveReload
- Watchdog
- FastAPI
- Uvicorn

✅ All server files created and executable

✅ Ready to use!

---

## Server Comparison Quick Reference

| Server | Auto-Reload | Browser Refresh | Speed | Best For |
|--------|-------------|-----------------|-------|----------|
| **LiveReload** ⭐ | All files | ✅ Automatic | Medium | Frontend dev |
| **Flask** | Python only | ❌ Manual | Medium | Backend dev |
| **FastAPI** | Python only | ❌ Manual | Fast | API dev |
| **Watchdog** | All files | ❌ Manual | Fast | Static files |

---

## Usage Examples

### Frontend Development (HTML/CSS/JS)
```bash
# Auto browser refresh on any file change!
python3 dev-server-livereload.py
```

**What happens:**
1. Server starts on port 8000
2. Open `http://0.0.0.0:8000` in browser
3. Edit any HTML/CSS/JS file
4. Browser automatically refreshes - no manual refresh needed!

### Backend Development (Python)
```bash
# Auto-reload Python files
python3 dev-server-flask.py
```

### API Development
```bash
# Fast server with auto-reload + API docs
python3 dev-fastapi.py

# Access:
# - Main: http://0.0.0.0:8000/
# - API Docs: http://0.0.0.0:8000/docs
# - Health: http://0.0.0.0:8000/health
```

### Terminal Game Development
```bash
# Auto-restart snake.py when you edit it
python3 dev-snake-watch.py
```

---

## Testing the Servers

### 1. Verify Installation
```bash
python3 test-server.py
```

Expected output:
```
📦 Dependency Check:
  Flask                ✓ Installed (v3.1.2)
  LiveReload           ✓ Installed
  Watchdog             ✓ Installed
  FastAPI              ✓ Installed

📄 Server Files Check:
  Flask Basic Server             ✓ File exists
  Flask LiveReload Server        ✓ File exists
  Watchdog File Watcher          ✓ File exists
  FastAPI Server                 ✓ File exists
  Snake Game Watcher             ✓ File exists
  Interactive Launcher           ✓ File exists
```

### 2. Test a Server
```bash
# Start LiveReload server (recommended)
python3 dev-server-livereload.py
```

You should see:
```
Flask Development Server with LiveReload
Server starting at: http://0.0.0.0:8000
Watching file types:
  - *.html
  - *.css
  - *.js
  - *.py
```

### 3. Test Auto-Reload
1. Start server: `python3 dev-server-livereload.py`
2. Open browser: `http://0.0.0.0:8000`
3. Edit `snake.html` - add a comment or change text
4. Save the file
5. **Browser automatically refreshes!** ✨

---

## Common Commands

```bash
# Start interactive launcher
./start-dev.sh

# Start specific server
python3 dev-server-livereload.py   # Best for frontend
python3 dev-server-flask.py         # Basic Flask
python3 dev-fastapi.py              # FastAPI
python3 dev-watch.py                # Watchdog

# Terminal game auto-restart
python3 dev-snake-watch.py

# Test setup
python3 test-server.py

# Install/reinstall dependencies
pip3 install -r requirements-dev.txt
```

---

## Features by Server

### dev-server-livereload.py ⭐ RECOMMENDED
```
✅ Auto-reload on HTML changes
✅ Auto-reload on CSS changes
✅ Auto-reload on JavaScript changes
✅ Auto-reload on Python changes
✅ Automatic browser refresh
✅ CORS enabled
```

### dev-server-flask.py
```
✅ Auto-reload on Python changes
✅ Debug mode with detailed errors
✅ CORS enabled
❌ Manual browser refresh for HTML/CSS/JS
```

### dev-fastapi.py
```
✅ Auto-reload on Python changes
✅ Ultra-fast ASGI server
✅ Automatic API documentation
✅ Modern async support
✅ CORS enabled
❌ Manual browser refresh
```

### dev-watch.py
```
✅ Monitors all file types
✅ Auto-restart server on changes
✅ Color-coded console output
✅ Lightweight
❌ Manual browser refresh
```

### dev-snake-watch.py
```
✅ Watches snake.py for changes
✅ Auto-restart terminal game
✅ Clean process management
✅ Perfect for game development
```

---

## Troubleshooting

### Server won't start - port in use
```bash
# Find what's using port 8000
lsof -i :8000

# Kill it
kill -9 <PID>
```

### Dependencies missing
```bash
# Reinstall everything
pip3 install -r requirements-dev.txt
```

### LiveReload not refreshing
1. Check browser console for errors
2. Hard refresh: Ctrl+Shift+R
3. Ensure you're editing files in the watched directory
4. Check file extension is being watched (.html, .css, .js, .py)

### Permission denied
```bash
# Make scripts executable
chmod +x start-dev.sh *.py
```

---

## File Structure

```
/home/user/claude-code-web-test/
├── 🎮 Game Files
│   ├── snake.html              # Web-based snake game
│   ├── snake.py                # Terminal snake game
│   └── index.html              # Project index
│
├── 🚀 Development Servers
│   ├── dev-server-flask.py           # Flask basic
│   ├── dev-server-livereload.py      # Flask + LiveReload ⭐
│   ├── dev-watch.py                  # Watchdog watcher
│   ├── dev-fastapi.py                # FastAPI server
│   └── dev-snake-watch.py            # Snake game watcher
│
├── 🔧 Utilities
│   ├── start-dev.sh                  # Interactive launcher
│   ├── test-server.py                # Test script
│   └── requirements-dev.txt          # Dependencies
│
└── 📚 Documentation
    ├── QUICK-START.md                # Quick start guide
    ├── DEV-SERVER-GUIDE.md          # Full documentation
    └── README-DEV-SERVERS.md        # This file
```

---

## Next Steps

1. **Try LiveReload** - Best experience!
   ```bash
   python3 dev-server-livereload.py
   ```

2. **Read Full Guide** - Learn all features
   ```bash
   cat DEV-SERVER-GUIDE.md
   ```

3. **Use Interactive Launcher** - Easy switching
   ```bash
   ./start-dev.sh
   ```

4. **Customize** - Modify servers for your needs
   - Change ports
   - Add file types to watch
   - Customize routes

---

## Advanced Usage

### Run Multiple Servers
```bash
# Terminal 1
python3 dev-server-livereload.py  # Port 8000

# Terminal 2 (edit port in file to 8001)
python3 dev-fastapi.py  # Port 8001
```

### Watch Custom File Types
Edit server files to add more file extensions:
```python
# In dev-server-livereload.py
server.watch(os.path.join(BASE_DIR, '*.json'))
server.watch(os.path.join(BASE_DIR, '*.md'))
```

### Custom Port
Edit the server file:
```python
# Flask servers
app.run(host='0.0.0.0', port=8080, debug=True)

# FastAPI
uvicorn.run(..., port=8080, ...)
```

---

## Production Notes

⚠️ **These servers are for DEVELOPMENT ONLY!**

For production, use:
- **Flask**: Gunicorn or uWSGI
- **FastAPI**: Uvicorn with workers (no --reload)

Example production commands:
```bash
# Flask with Gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:app

# FastAPI with Uvicorn
uvicorn app:app --host 0.0.0.0 --port 8000 --workers 4
```

---

## Summary

✅ **5 development servers** ready to use
✅ **All dependencies** installed
✅ **Full documentation** provided
✅ **Interactive launcher** for easy switching
✅ **Auto-reload** on file changes
✅ **LiveReload** with automatic browser refresh

**Recommended**: Start with `dev-server-livereload.py` for the best development experience!

```bash
python3 dev-server-livereload.py
```

Then open http://0.0.0.0:8000 and start coding! 🚀

---

**Happy developing!** 🎮✨

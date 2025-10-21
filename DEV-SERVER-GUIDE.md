# Python Development Servers with Auto-Reload

Complete guide to Python development servers with automatic reload capabilities.

## Quick Start

### Option 1: Interactive Launcher (Recommended)

```bash
chmod +x start-dev.sh
./start-dev.sh
```

This will show you a menu to choose your preferred server.

### Option 2: Direct Launch

```bash
# Flask with LiveReload (Best for frontend development)
python3 dev-server-livereload.py

# Flask basic (Simple and reliable)
python3 dev-server-flask.py

# Watchdog + HTTP server (Lightweight)
python3 dev-watch.py

# FastAPI (Best for API development)
python3 dev-fastapi.py

# Snake game watcher (Terminal game auto-restart)
python3 dev-snake-watch.py
```

---

## Server Comparison

| Feature | Flask Basic | Flask LiveReload | Watchdog | FastAPI |
|---------|-------------|------------------|----------|---------|
| **Auto-reload Python** | ✅ | ✅ | ✅ | ✅ |
| **Auto-reload HTML/CSS/JS** | ❌ | ✅ | ✅ | ❌ |
| **Browser auto-refresh** | ❌ | ✅ | ❌ | ❌ |
| **Speed** | Medium | Medium | Fast | Very Fast |
| **Setup complexity** | Low | Medium | Medium | Medium |
| **Best for** | Backend | Frontend | Static files | APIs |

### Recommendation

- **Frontend Development**: Use `dev-server-livereload.py` - automatic browser refresh!
- **Backend Development**: Use `dev-server-flask.py` or `dev-fastapi.py`
- **API Development**: Use `dev-fastapi.py` - includes automatic API docs
- **Simple Static Files**: Use `dev-watch.py`

---

## Installation

### Install All Dependencies

```bash
pip3 install -r requirements-dev.txt
```

### Or Install Individually

```bash
# For Flask servers
pip3 install flask flask-cors

# For LiveReload
pip3 install livereload

# For Watchdog
pip3 install watchdog

# For FastAPI
pip3 install fastapi uvicorn[standard]
```

---

## Server Details

### 1. Flask with Auto-Reload (`dev-server-flask.py`)

**Features:**
- Auto-reload on Python file changes
- Debug mode with detailed error messages
- CORS enabled for development
- Simple and reliable

**Usage:**
```bash
python3 dev-server-flask.py
```

**Access:**
- URL: `http://0.0.0.0:8000`
- Main page: `http://0.0.0.0:8000/`
- Any file: `http://0.0.0.0:8000/filename.html`

**Note:** HTML/CSS/JS changes require manual browser refresh.

---

### 2. Flask with LiveReload (`dev-server-livereload.py`) ⭐ RECOMMENDED

**Features:**
- Auto-reload on ANY file change (HTML, CSS, JS, Python)
- **Automatic browser refresh** - no manual refresh needed!
- LiveReload script auto-injected into HTML pages
- Watches multiple file types
- CORS enabled

**Usage:**
```bash
python3 dev-server-livereload.py
```

**How it works:**
1. Start the server
2. Open browser to `http://0.0.0.0:8000`
3. Edit any file (HTML, CSS, JS, Python)
4. Browser automatically refreshes!

**Perfect for:**
- Active frontend development
- Rapid prototyping
- CSS/HTML tweaking

---

### 3. Watchdog + HTTP Server (`dev-watch.py`)

**Features:**
- Monitors all Python, HTML, CSS, and JS files
- Automatically restarts Python HTTP server on changes
- Color-coded console output with timestamps
- Lightweight and fast
- Graceful shutdown and restart

**Usage:**
```bash
python3 dev-watch.py
```

**Console Output:**
```
[10:30:45] File changed: snake.html
[10:30:45] Restarting server...
[10:30:46] Server started at http://0.0.0.0:8000
```

**Perfect for:**
- Simple static file serving
- When you want to see file change notifications
- Lightweight development environment

---

### 4. FastAPI with Uvicorn (`dev-fastapi.py`)

**Features:**
- Ultra-fast ASGI server (faster than Flask)
- Auto-reload on Python file changes
- Modern async support
- **Automatic API documentation** at `/docs`
- Alternative docs at `/redoc`
- CORS enabled

**Usage:**
```bash
python3 dev-fastapi.py

# Or directly with uvicorn:
uvicorn dev-fastapi:app --reload --host 0.0.0.0 --port 8000
```

**Access:**
- Main page: `http://0.0.0.0:8000/`
- API docs: `http://0.0.0.0:8000/docs`
- Alternative docs: `http://0.0.0.0:8000/redoc`
- Health check: `http://0.0.0.0:8000/health`
- List files: `http://0.0.0.0:8000/api/files`

**Perfect for:**
- API development
- Modern async Python applications
- When you need built-in API documentation
- Performance-critical applications

---

### 5. Snake Game Terminal Watcher (`dev-snake-watch.py`)

**Features:**
- Watches `snake.py` for changes
- Automatically restarts the terminal game
- Clean process management
- Perfect for developing the terminal snake game

**Usage:**
```bash
python3 dev-snake-watch.py
```

**How it works:**
1. Starts `snake.py` terminal game
2. Watches for file changes
3. Automatically restarts game when you save changes
4. Clean shutdown on Ctrl+C

**Alternative (if you have `entr` installed):**
```bash
echo "snake.py" | entr -r python3 snake.py
```

---

## Interactive Launcher (`start-dev.sh`)

The interactive launcher provides a menu-driven interface:

```bash
chmod +x start-dev.sh
./start-dev.sh
```

**Menu Options:**
1. Flask (Basic Auto-Reload)
2. Flask + LiveReload [RECOMMENDED]
3. Watchdog + HTTP Server
4. FastAPI + Uvicorn
5. Install/Update Dependencies
6. Snake Game Terminal Watch
0. Exit

**Features:**
- Color-coded output
- Dependency installation
- Error checking
- Easy server switching

---

## Common Tasks

### Change Port

All servers use port 8000 by default. To change:

**Flask servers:**
```python
app.run(host='0.0.0.0', port=8080, debug=True)
```

**Watchdog server:**
```python
server_manager = ServerManager(port=8080)
```

**FastAPI:**
```python
uvicorn.run("dev-fastapi:app", host="0.0.0.0", port=8080, reload=True)
```

### Add File Type to Watch

**LiveReload:**
```python
server.watch(os.path.join(BASE_DIR, '*.json'))
```

**Watchdog:**
```python
if not any(event.src_path.endswith(ext) for ext in ['.py', '.html', '.css', '.js', '.json']):
    return
```

### Disable Auto-Reload

**Flask:**
```python
app.run(host='0.0.0.0', port=8000, debug=False, use_reloader=False)
```

**FastAPI:**
```python
uvicorn.run("dev-fastapi:app", host="0.0.0.0", port=8000, reload=False)
```

---

## Troubleshooting

### Port Already in Use

```bash
# Find process using port 8000
lsof -i :8000

# Kill the process
kill -9 <PID>

# Or use a different port
python3 dev-server-flask.py  # Edit port in file
```

### Dependencies Not Installed

```bash
# Install all dependencies
pip3 install -r requirements-dev.txt

# Or use the launcher
./start-dev.sh
# Choose option 5 to install dependencies
```

### LiveReload Not Working

1. Check browser console for errors
2. Ensure LiveReload script is injected
3. Try hard refresh (Ctrl+Shift+R)
4. Check file permissions

### File Changes Not Detected

1. Ensure file is in the watched directory
2. Check file extension is being watched
3. Look for error messages in console
4. Try manual restart

---

## Performance Tips

1. **Use LiveReload for frontend work** - saves time with auto-refresh
2. **Use FastAPI for APIs** - it's faster than Flask
3. **Exclude node_modules** - add to ignore patterns if watching subdirectories
4. **Use specific file patterns** - don't watch everything
5. **Set appropriate restart delays** - avoid too frequent restarts

---

## Advanced Usage

### Multiple Servers

Run multiple servers on different ports:

```bash
# Terminal 1
python3 dev-server-flask.py  # Port 8000

# Terminal 2 (edit port in file first)
python3 dev-fastapi.py  # Port 8001
```

### Custom File Watcher

Create your own watcher for specific needs:

```python
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class CustomHandler(FileSystemEventHandler):
    def on_modified(self, event):
        # Your custom logic here
        pass

observer = Observer()
observer.schedule(CustomHandler(), '.', recursive=True)
observer.start()
```

### Production Deployment

**Note:** These development servers are NOT for production use!

For production, use:
- **Flask**: Gunicorn or uWSGI
- **FastAPI**: Uvicorn with workers (no --reload flag)

Example production command:
```bash
# Flask with Gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:app

# FastAPI with Uvicorn
uvicorn app:app --host 0.0.0.0 --port 8000 --workers 4
```

---

## Summary

- **Best Overall**: `dev-server-livereload.py` - auto-refresh is amazing!
- **Simplest**: `dev-server-flask.py` - just works
- **Fastest**: `dev-fastapi.py` - modern and performant
- **Most Flexible**: `dev-watch.py` - custom file watching

All servers include:
- Auto-reload on file changes
- CORS enabled for development
- Helpful error messages
- Easy to use and modify

Choose the one that fits your workflow best!

---

## Files Created

```
/home/user/claude-code-web-test/
├── dev-server-flask.py           # Flask with basic auto-reload
├── dev-server-livereload.py      # Flask with LiveReload (RECOMMENDED)
├── dev-watch.py                  # Watchdog file watcher
├── dev-fastapi.py                # FastAPI with uvicorn
├── dev-snake-watch.py            # Snake game terminal watcher
├── start-dev.sh                  # Interactive launcher script
├── requirements-dev.txt          # Python dependencies
└── DEV-SERVER-GUIDE.md          # This guide
```

---

**Happy developing!** 🚀

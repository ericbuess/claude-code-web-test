# Quick Start - Python Development Servers

## 30 Second Setup

```bash
# Install dependencies
pip3 install flask flask-cors livereload watchdog fastapi uvicorn[standard]

# Launch interactive menu
./start-dev.sh
```

## One Command Launch

```bash
# RECOMMENDED: Flask + LiveReload (auto browser refresh!)
python3 dev-server-livereload.py

# Then open: http://0.0.0.0:8000
```

## Cheat Sheet

| Server | Command | Best For |
|--------|---------|----------|
| **LiveReload** ⭐ | `python3 dev-server-livereload.py` | Frontend dev (auto-refresh!) |
| **Flask** | `python3 dev-server-flask.py` | Backend dev |
| **FastAPI** | `python3 dev-fastapi.py` | API dev |
| **Watchdog** | `python3 dev-watch.py` | Static files |
| **Snake Watch** | `python3 dev-snake-watch.py` | Terminal game dev |

## What You Get

- ✅ Auto-reload on file changes
- ✅ No manual browser refresh (LiveReload)
- ✅ Multiple server options
- ✅ Easy to switch between servers
- ✅ CORS enabled for development

## Next Steps

1. Read [DEV-SERVER-GUIDE.md](DEV-SERVER-GUIDE.md) for full documentation
2. Edit `requirements-dev.txt` to customize dependencies
3. Modify server scripts to fit your needs

**Happy coding!** 🎮

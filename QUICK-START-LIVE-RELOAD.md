# Quick Start: Live Reload Development

One-page guide to get started with live reload development for the Snake game.

## Fastest Way to Start

```bash
# Option 1: Live-Server (Simple & Fast)
./dev-server.sh

# Option 2: Browser-Sync (Advanced Features)
./dev-browsersync.sh

# Option 3: NPM Scripts
npm run dev:live         # Live-Server
npm run dev:browsersync  # Browser-Sync
```

## What You Get

### Live-Server
- **URL:** http://localhost:8080
- **Auto-reload:** Yes (~200ms response)
- **Best for:** Quick development, simple projects

### Browser-Sync
- **Main URL:** http://localhost:3000
- **UI Dashboard:** http://localhost:3001
- **Auto-reload:** Yes (~100ms response - FASTER)
- **Best for:** Multi-device testing, advanced development
- **Bonus:** Synchronized scrolling, clicks across devices

### HTTP-Server
- **URL:** http://localhost:8081
- **Auto-reload:** NO
- **Best for:** Static file serving without reload

## How Auto-Reload Works

1. Start the server
2. Open browser to the URL
3. Edit any .html, .js, or .css file
4. Save the file
5. Browser automatically refreshes (no F5 needed!)

## Test Results (Verified)

All tests PASSED:

- Live-Server: Auto-reload working
- Browser-Sync: Auto-reload working
- Response times: 100-200ms
- File detection: Immediate
- Browser refresh: Automatic

## Installation (Already Done)

If you need to install on another machine:

```bash
npm install -g live-server
npm install -g browser-sync
```

## Full Documentation

See `LIVE-RELOAD-SETUP.md` for complete documentation.

## Troubleshooting

**Port in use?**
- Live-Server automatically finds next available port
- Browser-Sync: Edit script and change `--port 3000` to another number

**Not reloading?**
- Check console for "Change detected" messages
- Verify you saved the file
- Make sure file is .html, .js, or .css

**Need to stop server?**
- Press `Ctrl+C` in the terminal

## Run Tests

Verify everything works:

```bash
./test-live-reload.sh
```

All servers should pass their tests.

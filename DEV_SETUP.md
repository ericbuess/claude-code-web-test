# Modern Development Setup Guide

This guide covers all the modern development tools configured for the Snake Game project with Hot Module Replacement (HMR) and auto-deployment.

## Quick Start

### Option 1: Vite (Recommended - Fastest)
```bash
npm run dev
```
- Startup time: ~100-300ms
- Instant HMR
- Opens at: http://localhost:3000
- Lightning fast rebuilds

### Option 2: Parcel (Zero Config)
```bash
npm run dev:parcel
```
- Zero configuration required
- Auto HMR
- Opens at: http://localhost:3001

### Option 3: Live Server
```bash
npm run dev:live
```
- Simple HTTP server with live reload
- Opens at: http://localhost:8080

### Option 4: Browser-Sync
```bash
npm run dev:browsersync
```
- Cross-device testing
- UI for controlling reloads
- Opens at: http://localhost:3000

## All Available Scripts

```json
{
  "dev": "vite",                    // Start Vite dev server (recommended)
  "dev:vite": "vite",               // Explicit Vite server
  "dev:parcel": "parcel snake.html", // Start Parcel dev server
  "build": "vite build",            // Production build with Vite
  "preview": "vite preview",        // Preview production build
  "auto-deploy": "node auto-deploy.js", // Auto-deploy on file changes
  "watch": "node auto-deploy.js"    // Alias for auto-deploy
}
```

## Why Vite?

Vite is the **fastest** modern development tool because:

1. **No Bundling During Dev**: Serves native ES modules directly
2. **Instant HMR**: Changes appear in <100ms
3. **Fast Cold Start**: Server starts in ~100-300ms
4. **Optimized Production Builds**: Uses Rollup for production

### Performance Comparison

| Server | Startup Time | HMR Speed | Configuration |
|--------|--------------|-----------|---------------|
| Vite | ~100-300ms | <100ms | Minimal |
| Parcel | ~1-2s | ~200-500ms | Zero |
| Live Server | ~50ms | ~500ms (full reload) | None |
| Browser-Sync | ~500ms | ~500ms (full reload) | Some |

## Vite Configuration

File: `vite.config.js`

```javascript
import { defineConfig } from 'vite'

export default defineConfig({
  root: '.',
  server: {
    port: 3000,
    open: true,
    host: true
  },
  build: {
    outDir: 'dist',
    emptyOutDir: true
  }
})
```

## Auto-Deploy Setup

The auto-deploy script watches for file changes and automatically commits and pushes to GitHub.

### Features:
- Watches HTML, CSS, and JS files
- Auto-commits with timestamps
- Auto-pushes to GitHub
- CDN URLs update automatically in 1-2 minutes

### Usage:
```bash
npm run auto-deploy
# or
npm run watch
```

### How it works:
1. Watches for changes in `*.html`, `*.css`, `*.js` files
2. When a file changes, automatically:
   - Runs `git add .`
   - Commits with timestamp: `Auto-update: filename (timestamp)`
   - Pushes to GitHub: `git push`
3. GitHub Pages / CDN picks up changes automatically

### Configuration:
Edit `auto-deploy.js` to customize:
- Watch patterns
- Ignored files
- Commit message format

## Development Workflow

### Recommended Workflow (Fastest Development):

1. **Start Vite dev server**:
   ```bash
   npm run dev
   ```

2. **Edit files in your IDE** - changes appear instantly

3. **(Optional) Enable auto-deploy in another terminal**:
   ```bash
   npm run watch
   ```

### Testing Different Servers:

Run the benchmark script to compare all servers:
```bash
node benchmark-dev-servers.js
```

This will test:
- Startup time for each server
- HMR performance
- Overall developer experience

## Hot Module Replacement (HMR)

### What is HMR?
HMR updates your application in the browser **without a full page reload**, preserving application state.

### Vite HMR Features:
- Updates CSS instantly
- Preserves game state during updates
- Extremely fast (<100ms)
- No configuration needed

### Testing HMR:
1. Start dev server: `npm run dev`
2. Open the game in browser
3. Make a change to `snake.html` (e.g., change colors)
4. Watch the change appear instantly without reload

## Production Build

### Build for production:
```bash
npm run build
```

This creates an optimized production build in the `dist/` directory.

### Preview production build:
```bash
npm run preview
```

Opens the production build at http://localhost:4173

## Troubleshooting

### Port already in use:
Change the port in `vite.config.js`:
```javascript
server: {
  port: 3001  // Use a different port
}
```

### Auto-deploy not working:
1. Ensure git is configured
2. Check you have push permissions
3. Verify the remote branch exists

### HMR not updating:
1. Check browser console for errors
2. Try clearing cache: Ctrl+Shift+R (Windows/Linux) or Cmd+Shift+R (Mac)
3. Restart the dev server

## Dependencies

All dependencies are installed via npm:

```json
{
  "devDependencies": {
    "vite": "^7.1.11",      // Fast dev server with HMR
    "parcel": "^2.16.0",    // Zero-config bundler
    "chokidar": "^4.0.3"    // File watcher for auto-deploy
  }
}
```

## CDN URLs (GitHub Pages)

After deployment, your game is available at:
- https://cdn.jsdelivr.net/gh/YOUR_USERNAME/claude-code-web-test@main/snake.html
- https://YOUR_USERNAME.github.io/claude-code-web-test/snake.html

Changes pushed to GitHub appear in ~1-2 minutes.

## Best Practices

1. **Use Vite for development** - It's the fastest
2. **Enable auto-deploy only when needed** - Avoid committing every keystroke
3. **Test production builds** - Run `npm run build` before deploying
4. **Use HMR effectively** - Make small, iterative changes
5. **Keep dev dependencies up to date** - Run `npm update` regularly

## Resources

- [Vite Documentation](https://vitejs.dev/)
- [Parcel Documentation](https://parceljs.org/)
- [Chokidar Documentation](https://github.com/paulmillr/chokidar)
- [GitHub Pages Documentation](https://docs.github.com/en/pages)

## Summary

**Fastest Development Setup:**
```bash
npm run dev  # Vite dev server - instant HMR
```

**Auto-Deploy Setup:**
```bash
npm run watch  # Auto-deploy on file changes
```

**Production Build:**
```bash
npm run build  # Optimized production build
npm run preview  # Preview production build
```

Enjoy lightning-fast development with instant Hot Module Replacement!

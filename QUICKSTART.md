# Quick Start Guide

## Installation

```bash
npm install
```

## Start Development Server

### Fastest Option (Vite - Recommended)
```bash
npm run dev
```
Opens at: http://localhost:3000

**Features:**
- Startup: ~100-300ms
- HMR: <100ms (instant updates)
- No bundling during development
- Automatic browser open

### Alternative Options

#### Parcel (Zero Config)
```bash
npm run dev:parcel
```
Opens at: http://localhost:3001

#### Live Server
```bash
npm run dev:live
```
Opens at: http://localhost:8080

## Auto-Deploy (Optional)

Watch files and auto-commit/push to GitHub on changes:

```bash
npm run watch
```

**What it does:**
1. Watches for changes in HTML, CSS, JS files
2. Auto-commits with timestamp
3. Auto-pushes to GitHub
4. CDN updates in 1-2 minutes

## Production Build

```bash
npm run build
```

Creates optimized build in `dist/` directory.

Preview build:
```bash
npm run preview
```

## Testing

Run performance benchmark:
```bash
node benchmark-dev-servers.js
```

Compares startup and HMR performance of all dev servers.

## Live URLs

After deployment:
- **GitHub Pages**: https://YOUR_USERNAME.github.io/claude-code-web-test/snake.html
- **jsDelivr CDN**: https://cdn.jsdelivr.net/gh/YOUR_USERNAME/claude-code-web-test@main/snake.html

## Commands Summary

| Command | Description |
|---------|-------------|
| `npm run dev` | Start Vite dev server (fastest) |
| `npm run dev:parcel` | Start Parcel dev server |
| `npm run build` | Build for production |
| `npm run preview` | Preview production build |
| `npm run watch` | Auto-deploy on changes |

## Recommended Workflow

1. Install: `npm install`
2. Develop: `npm run dev`
3. Edit files - see instant updates
4. Build: `npm run build`
5. Deploy: Push to GitHub

**That's it!** Vite provides the fastest development experience with instant Hot Module Replacement.

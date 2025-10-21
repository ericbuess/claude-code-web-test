# 🔥 HOT RELOAD WITH EXTERNAL ACCESS

## The Solution: Auto-Deploy to GitHub Pages/CDN

Since the environment has network restrictions, we can't expose local servers externally. Instead, we use **auto-deployment**: file changes automatically push to GitHub, and CDN URLs update within seconds.

---

## 🚀 QUICK START

### Step 1: Enable GitHub Pages (One-time setup)

1. Go to: https://github.com/ericbuess/claude-code-web-test/settings/pages
2. Source: `claude/snake-game-implementation-011CUJv4XruvjB9d6bpZkCiT`
3. Folder: `/ (root)`
4. Click **Save**

### Step 2: Start Auto-Deploy Watcher

```bash
./watch-and-deploy.sh
```

### Step 3: Open External URL

```
https://raw.githack.com/ericbuess/claude-code-web-test/claude/snake-game-implementation-011CUJv4XruvjB9d6bpZkCiT/snake.html
```

### Step 4: Make Changes & Watch

1. Edit `snake.html` in your editor
2. Save the file
3. Watch script auto-commits and pushes
4. Wait 30-120 seconds
5. **Refresh browser** to see changes

---

## 🌐 YOUR EXTERNAL URLs

### Option 1: RawGitHack (Fastest Updates - 30 sec)
```
https://raw.githack.com/ericbuess/claude-code-web-test/claude/snake-game-implementation-011CUJv4XruvjB9d6bpZkCiT/snake.html
```

### Option 2: GitHub Pages (Clean URL - need to enable)
```
https://ericbuess.github.io/claude-code-web-test/snake.html
```

### Option 3: jsDelivr CDN (1-2 min updates)
```
https://cdn.jsdelivr.net/gh/ericbuess/claude-code-web-test@claude/snake-game-implementation-011CUJv4XruvjB9d6bpZkCiT/snake.html
```

---

## 📊 How It Works

```
You edit file
    ↓
Save (Ctrl+S)
    ↓
watch-and-deploy.sh detects change
    ↓
Auto git add + commit + push
    ↓
GitHub receives update (5 seconds)
    ↓
GitHub Pages rebuilds (15-60 seconds)
    ↓
CDN caches update (30-120 seconds)
    ↓
You refresh browser → SEE CHANGES! 🎉
```

**Total time:** 30 seconds - 2 minutes (vs true HMR: <100ms)

---

## 🎯 Development Workflow

### Traditional Hot Reload (Local Only)
```bash
# For local development (can't access externally)
npm run dev              # Vite - <100ms HMR
npm run dev:live         # Live-server
npm run dev:browsersync  # Browser-sync
```

### External Access Hot Reload (This Solution)
```bash
# For external access - auto-deploy on save
./watch-and-deploy.sh

# Then open in YOUR browser:
https://raw.githack.com/.../snake.html
```

---

## 📝 What Happens When You Save

```bash
$ ./watch-and-deploy.sh

🚀 Starting Auto-Deploy Watch Server
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📡 EXTERNAL ACCESS URLs (will auto-update):

1. GitHub Pages: https://ericbuess.github.io/claude-code-web-test/snake.html
2. RawGitHack: https://raw.githack.com/.../snake.html
3. jsDelivr: https://cdn.jsdelivr.net/.../snake.html

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

👀 Watching for changes in: *.html, *.js, *.css, *.py
💾 Auto-commit & push on file save
⏱️  CDN updates: 30 seconds - 2 minutes
🔄 Press Ctrl+C to stop

🔔 Change detected: snake.html
📝 Committing...
🚀 Pushing to GitHub...
✅ Pushed successfully!
⏱️  CDN will update in 30-120 seconds
🔄 Refresh your browser to see changes
```

---

## 🧪 Test The Auto-Reload

### Test Steps:

1. **Start watcher:**
   ```bash
   ./watch-and-deploy.sh
   ```

2. **Open external URL in browser:**
   ```
   https://raw.githack.com/ericbuess/claude-code-web-test/claude/snake-game-implementation-011CUJv4XruvjB9d6bpZkCiT/snake.html
   ```

3. **Make a visible change:**
   Edit line 134 in `snake.html`:
   ```html
   <h1>🐍 Snake Game</h1>
   ```
   Change to:
   ```html
   <h1>🐍 Snake Game - LIVE RELOAD TEST! 🔥</h1>
   ```

4. **Save file** (Ctrl+S)

5. **Watch terminal** - should show auto-commit & push

6. **Wait 30-120 seconds**

7. **Refresh browser** - see the change!

---

## 🎨 Python Auto-Reload (Local Terminal)

For the Python snake game:

```bash
# Watch and auto-restart Python game
python3 dev-snake-watch.py
```

This monitors `snake.py` and auto-restarts the terminal game on changes (local only).

---

## 🔧 Advanced: Manual Control

### Start/Stop Auto-Deploy
```bash
# Start watching
./watch-and-deploy.sh

# Stop watching
Press Ctrl+C
```

### Manual Deploy (no watching)
```bash
git add snake.html
git commit -m "Update game"
git push
```

### Clear CDN Cache (force update)
```bash
# jsDelivr purge
curl https://purge.jsdelivr.net/gh/ericbuess/claude-code-web-test@claude/snake-game-implementation-011CUJv4XruvjB9d6bpZkCiT/snake.html
```

---

## ⚡ Performance Comparison

| Method | Update Speed | External Access | Auto-Reload |
|--------|-------------|-----------------|-------------|
| Vite HMR | <100ms | ❌ No | ✅ Yes |
| Live-server | Instant | ❌ No | ✅ Yes |
| Browser-Sync | Instant | ❌ No | ✅ Yes |
| **Auto-Deploy** | **30-120s** | **✅ Yes** | **✅ Semi** |

**Trade-off:** Slower updates BUT accessible from anywhere!

---

## 🎯 Best Workflow

### For YOU (external user):
```bash
./watch-and-deploy.sh
# Open: https://raw.githack.com/.../snake.html
# Edit files, save, wait 30s, refresh browser
```

### For local development (inside environment):
```bash
npm run dev
# Open: http://localhost:5173
# Edit files, see changes instantly (<100ms)
```

---

## 🐛 Troubleshooting

### Changes not showing up?

1. **Check if pushed:**
   ```bash
   git log -1
   # Should show recent auto-commit
   ```

2. **Force CDN refresh:**
   - Add `?v=timestamp` to URL
   - Hard refresh: Ctrl+Shift+R
   - Clear browser cache

3. **Check GitHub:**
   - Visit: https://github.com/ericbuess/claude-code-web-test
   - Verify latest commit is there

### Watch script not detecting changes?

```bash
# Check if chokidar is installed
which chokidar

# Reinstall if needed
npm install -g chokidar-cli

# Test manually
chokidar "snake.html" -c "echo Changed: {path}"
```

---

## 📚 Files Created

- `.github/workflows/deploy.yml` - GitHub Actions auto-deploy
- `watch-and-deploy.sh` - File watcher with auto-push
- `HOT_RELOAD_EXTERNAL.md` - This guide

---

## 🎉 Summary

**You now have:**
- ✅ External URLs you can access from anywhere
- ✅ Auto-deployment on file save
- ✅ "Hot reload" (30-120 second delay)
- ✅ GitHub Pages integration
- ✅ CDN distribution
- ✅ No manual git commands needed

**To use:**
```bash
./watch-and-deploy.sh
```

**Access at:**
```
https://raw.githack.com/ericbuess/claude-code-web-test/claude/snake-game-implementation-011CUJv4XruvjB9d6bpZkCiT/snake.html
```

**Make changes, save, wait 30s, refresh browser!** 🚀

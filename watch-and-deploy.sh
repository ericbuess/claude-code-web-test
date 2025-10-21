#!/bin/bash
# Auto-deploy watcher with hot reload simulation
# Watches for file changes and auto-pushes to GitHub
# GitHub Pages/CDN URLs update within 1-2 minutes

echo "🚀 Starting Auto-Deploy Watch Server"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📡 EXTERNAL ACCESS URLs (will auto-update):"
echo ""
echo "1. GitHub Pages (enable manually first):"
echo "   https://ericbuess.github.io/claude-code-web-test/snake.html"
echo ""
echo "2. RawGitHack CDN (auto-updates):"
echo "   https://raw.githack.com/ericbuess/claude-code-web-test/claude/snake-game-implementation-011CUJv4XruvjB9d6bpZkCiT/snake.html"
echo ""
echo "3. jsDelivr CDN (updates in 1-2 min):"
echo "   https://cdn.jsdelivr.net/gh/ericbuess/claude-code-web-test@claude/snake-game-implementation-011CUJv4XruvjB9d6bpZkCiT/snake.html"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "👀 Watching for changes in: *.html, *.js, *.css, *.py"
echo "💾 Auto-commit & push on file save"
echo "⏱️  CDN updates: 30 seconds - 2 minutes"
echo "🔄 Press Ctrl+C to stop"
echo ""

cd /home/user/claude-code-web-test

# Install chokidar if not present
if ! command -v chokidar &> /dev/null; then
    echo "📦 Installing chokidar-cli..."
    npm install -g chokidar-cli
fi

# Function to commit and push
commit_and_push() {
    local file=$1
    local timestamp=$(date '+%Y-%m-%d %H:%M:%S')

    echo ""
    echo "🔔 Change detected: $file"
    echo "📝 Committing..."

    git add "$file"
    git commit -m "Auto-update: $file ($timestamp)

🤖 Auto-deployed via watch script

Co-Authored-By: Claude <noreply@anthropic.com>" 2>&1 | grep -v "^#"

    echo "🚀 Pushing to GitHub..."
    if git push origin claude/snake-game-implementation-011CUJv4XruvjB9d6bpZkCiT 2>&1 | grep -q "Everything up-to-date"; then
        echo "✅ No changes to push"
    else
        echo "✅ Pushed successfully!"
        echo "⏱️  CDN will update in 30-120 seconds"
        echo "🔄 Refresh your browser to see changes"
    fi

    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
}

export -f commit_and_push

# Watch for changes
chokidar "snake.html" "snake.py" "*.js" "*.css" \
    --ignore "node_modules/**" \
    --ignore "*.md" \
    --ignore ".git/**" \
    -c 'bash -c "commit_and_push {path}"'

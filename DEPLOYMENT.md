# Snake Game - Deployment Guide

## WORKING URLs (Available NOW)

The Snake game is already live and accessible via these free CDN services:

### 1. Raw.GitHack.com (RECOMMENDED - Fast CDN)
```
https://raw.githack.com/ericbuess/claude-code-web-test/claude/snake-game-implementation-011CUJv4XruvjB9d6bpZkCiT/snake.html
```

### 2. Statically.io CDN
```
https://cdn.statically.io/gh/ericbuess/claude-code-web-test/claude/snake-game-implementation-011CUJv4XruvjB9d6bpZkCiT/snake.html
```

### 3. jsDelivr CDN
```
https://cdn.jsdelivr.net/gh/ericbuess/claude-code-web-test@claude/snake-game-implementation-011CUJv4XruvjB9d6bpZkCiT/snake.html
```

### 4. HTMLPreview.GitHub.io
```
https://htmlpreview.github.io/?https://github.com/ericbuess/claude-code-web-test/blob/claude/snake-game-implementation-011CUJv4XruvjB9d6bpZkCiT/snake.html
```

## GitHub Pages Setup (Manual Steps Required)

Since GitHub Pages requires repository owner permissions, follow these steps:

### Option 1: Enable via GitHub Web Interface (Easiest)

1. Go to: https://github.com/ericbuess/claude-code-web-test/settings/pages
2. Under "Source", select the branch: `claude/snake-game-implementation-011CUJv4XruvjB9d6bpZkCiT`
3. Select folder: `/ (root)`
4. Click "Save"
5. Wait 1-2 minutes for deployment
6. Access at: `https://ericbuess.github.io/claude-code-web-test/snake.html`

### Option 2: Using gh-pages Branch (Traditional Method)

1. Create and push gh-pages branch:
   ```bash
   git checkout -b gh-pages
   git push origin gh-pages
   ```
2. Go to Settings > Pages
3. Select `gh-pages` branch
4. Game will be available at: `https://ericbuess.github.io/claude-code-web-test/snake.html`

### Option 3: Using GitHub CLI (if authenticated)

```bash
# Install gh CLI if not available
# brew install gh  # macOS
# apt install gh   # Ubuntu/Debian

# Enable Pages
gh api repos/ericbuess/claude-code-web-test/pages \
  --method POST \
  -f source[branch]=claude/snake-game-implementation-011CUJv4XruvjB9d6bpZkCiT \
  -f source[path]=/
```

## Alternative Free Hosting Platforms

### Surge.sh
```bash
npm install -g surge
cd /path/to/directory/with/snake.html
surge
# Follow prompts to create account and deploy
```

### Netlify
```bash
npm install -g netlify-cli
netlify login
netlify deploy --prod --dir=.
```

### Vercel
```bash
npm install -g vercel
vercel login
vercel --prod
```

## Quick Test Links

### Direct GitHub Raw Content (No HTML rendering)
```
https://raw.githubusercontent.com/ericbuess/claude-code-web-test/claude/snake-game-implementation-011CUJv4XruvjB9d6bpZkCiT/snake.html
```

### GitHub Blob View
```
https://github.com/ericbuess/claude-code-web-test/blob/claude/snake-game-implementation-011CUJv4XruvjB9d6bpZkCiT/snake.html
```

## Troubleshooting

### CDN URLs not working?
- These services might take a few minutes to cache the content
- Try clearing your browser cache
- Verify the branch name is correct

### GitHub Pages not deploying?
- Check that the branch exists and contains snake.html
- Ensure Pages is enabled in repository settings
- Check the Actions tab for deployment status
- Wait 2-5 minutes after enabling Pages

### Alternative: Create index.html
If you want the game at the root URL, copy snake.html to index.html:
```bash
cp snake.html index.html
git add index.html
git commit -m "Add index.html for root access"
git push
```

Then access at: `https://ericbuess.github.io/claude-code-web-test/`

## Browser Compatibility

The Snake game works in all modern browsers:
- Chrome/Edge (v90+)
- Firefox (v88+)
- Safari (v14+)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Features

- Responsive design
- Mobile touch controls
- Sound effects (toggle on/off)
- High score tracking (localStorage)
- Pause functionality
- Smooth animations

## Support

For issues or questions:
- GitHub Issues: https://github.com/ericbuess/claude-code-web-test/issues
- Repository: https://github.com/ericbuess/claude-code-web-test

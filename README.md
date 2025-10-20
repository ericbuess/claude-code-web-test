# Claude Code Web Test - Snake Game

A fully-featured, responsive Snake game built with vanilla HTML, CSS, and JavaScript.

## Play Now!

The game is live and ready to play at these URLs:

### Primary URL (Recommended)
```
https://raw.githack.com/ericbuess/claude-code-web-test/claude/snake-game-implementation-011CUJv4XruvjB9d6bpZkCiT/snake.html
```

### Alternative CDN URLs
- **Statically.io:** https://cdn.statically.io/gh/ericbuess/claude-code-web-test/claude/snake-game-implementation-011CUJv4XruvjB9d6bpZkCiT/snake.html
- **jsDelivr:** https://cdn.jsdelivr.net/gh/ericbuess/claude-code-web-test@claude/snake-game-implementation-011CUJv4XruvjB9d6bpZkCiT/snake.html
- **HTMLPreview:** https://htmlpreview.github.io/?https://github.com/ericbuess/claude-code-web-test/blob/claude/snake-game-implementation-011CUJv4XruvjB9d6bpZkCiT/snake.html

## Features

- **Beautiful UI**: Modern gradient design with glassmorphism effects
- **Responsive**: Works on desktop, tablet, and mobile devices
- **Touch Controls**: On-screen buttons for mobile gameplay
- **Sound Effects**: Toggle-able audio feedback
- **High Score**: Persistent high score tracking using localStorage
- **Smooth Animations**: Pulsing food animation and directional snake eyes
- **Pause Function**: Press SPACE to pause/resume

## How to Play

1. **Desktop**: Use arrow keys to control the snake
2. **Mobile**: Tap the on-screen directional buttons
3. **Pause**: Press SPACE to pause/resume
4. **Sound**: Click the sound button to toggle audio on/off
5. **Restart**: Click "Restart Game" button after game over

## Controls

- Up Arrow: Move up
- Down Arrow: Move down
- Left Arrow: Move left
- Right Arrow: Move right
- Space: Pause/Resume

## Game Mechanics

- Eat the red pulsing food to grow and score points
- Don't hit the walls
- Don't collide with your own tail
- Each food item gives you 10 points
- Try to beat your high score!

## Files

- `snake.html` - Main game file (self-contained, no dependencies)
- `index.html` - Copy of snake.html for root URL access
- `snake.py` - Python/Pygame version of the game
- `LIVE_URLS.md` - Complete list of live deployment URLs
- `DEPLOYMENT.md` - Deployment guide and hosting options

## Local Development

To run locally, simply open the HTML file:

```bash
# Clone the repository
git clone https://github.com/ericbuess/claude-code-web-test.git

# Navigate to directory
cd claude-code-web-test

# Open in browser (choose one)
open snake.html              # macOS
xdg-open snake.html          # Linux
start snake.html             # Windows
```

Or use a local server:

```bash
# Python 3
python -m http.server 8000

# Python 2
python -m SimpleHTTPServer 8000

# Node.js
npx http-server
```

Then visit: `http://localhost:8000/snake.html`

## GitHub Pages Setup

To enable GitHub Pages for permanent hosting:

1. Go to [Repository Settings > Pages](https://github.com/ericbuess/claude-code-web-test/settings/pages)
2. Select source branch: `claude/snake-game-implementation-011CUJv4XruvjB9d6bpZkCiT`
3. Select folder: `/ (root)`
4. Click "Save"
5. Game will be available at: `https://ericbuess.github.io/claude-code-web-test/`

## Technology Stack

- **HTML5**: Semantic markup and Canvas API
- **CSS3**: Modern styling with gradients, shadows, and animations
- **JavaScript**: Vanilla ES6+ (no frameworks/libraries)
- **Web Audio API**: Sound effects generation
- **LocalStorage API**: High score persistence

## Browser Compatibility

Works in all modern browsers:
- Chrome/Edge 90+
- Firefox 88+
- Safari 14+
- Mobile browsers (iOS Safari, Chrome Mobile)

## Python Version

A Python/Pygame version is also available in `snake.py`. To run:

```bash
pip install pygame
python snake.py
```

## Testing

Comprehensive tests are available in the `tests/` directory. See the Python implementation for unit tests and integration tests.

## Contributing

This is a demonstration project. Feel free to fork and modify!

## License

MIT License - feel free to use this code for learning and projects.

## Credits

Created with Claude Code - Anthropic's AI assistant for coding.

---

**Play the game now:** [Click here to play!](https://raw.githack.com/ericbuess/claude-code-web-test/claude/snake-game-implementation-011CUJv4XruvjB9d6bpZkCiT/snake.html)

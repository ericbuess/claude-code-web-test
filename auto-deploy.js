#!/usr/bin/env node

/**
 * Auto-Deploy Script
 * Watches for file changes and automatically commits/pushes to GitHub
 * This enables instant CDN updates via GitHub Pages
 */

const chokidar = require('chokidar');
const { execSync } = require('child_process');
const path = require('path');

// Files to watch
const watchPatterns = ['snake.html', 'index.html', '*.css', '*.js'];

// Files to ignore
const ignored = [
  '**/node_modules/**',
  '**/.git/**',
  '**/dist/**',
  '**/.parcel-cache/**',
  '**/auto-deploy.js',
  '**/test_*.js'
];

let isDeploying = false;
let changeQueue = [];

console.log('Auto-Deploy Watcher Started');
console.log('Watching files:', watchPatterns.join(', '));
console.log('Press Ctrl+C to stop\n');

// Initialize watcher
const watcher = chokidar.watch(watchPatterns, {
  ignored: ignored,
  persistent: true,
  ignoreInitial: true
});

// Git commands
function gitStatus() {
  try {
    return execSync('git status --porcelain', { encoding: 'utf-8' });
  } catch (error) {
    console.error('Error checking git status:', error.message);
    return '';
  }
}

function deployChanges(filePath) {
  if (isDeploying) {
    changeQueue.push(filePath);
    return;
  }

  isDeploying = true;
  const timestamp = new Date().toISOString();
  const fileName = path.basename(filePath);

  try {
    // Check if there are changes
    const status = gitStatus();
    if (!status) {
      console.log(`No changes to deploy for ${fileName}`);
      isDeploying = false;
      processQueue();
      return;
    }

    console.log(`\nDeploying changes for: ${fileName}`);
    console.log(`Time: ${timestamp}`);

    // Add changed files
    execSync('git add .', { stdio: 'inherit' });

    // Commit with timestamp
    const commitMessage = `Auto-update: ${fileName} (${timestamp})`;
    execSync(`git commit -m "${commitMessage}"`, { stdio: 'inherit' });

    // Push to remote
    console.log('Pushing to GitHub...');
    execSync('git push', { stdio: 'inherit' });

    console.log('Deployment successful!');
    console.log('CDN URLs will update automatically in ~1-2 minutes');
    console.log('Waiting for changes...\n');

  } catch (error) {
    console.error('Deployment error:', error.message);
  } finally {
    isDeploying = false;
    processQueue();
  }
}

function processQueue() {
  if (changeQueue.length > 0) {
    const nextFile = changeQueue.shift();
    // Wait a bit before processing next change
    setTimeout(() => deployChanges(nextFile), 1000);
  }
}

// Event handlers
watcher
  .on('change', (filePath) => {
    console.log(`File changed: ${filePath}`);
    deployChanges(filePath);
  })
  .on('add', (filePath) => {
    console.log(`File added: ${filePath}`);
    deployChanges(filePath);
  })
  .on('error', (error) => {
    console.error('Watcher error:', error);
  });

// Handle graceful shutdown
process.on('SIGINT', () => {
  console.log('\nStopping auto-deploy watcher...');
  watcher.close();
  process.exit(0);
});

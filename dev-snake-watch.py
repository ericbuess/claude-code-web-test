#!/usr/bin/env python3
"""
Snake Game Terminal Watcher
============================

Automatically restarts snake.py when the file changes.
Perfect for developing the terminal snake game!

Installation:
    pip3 install watchdog

Usage:
    python3 dev-snake-watch.py

Features:
- Monitors snake.py for changes
- Automatically restarts the game
- Clean process management
- Keyboard interrupt handling
"""

import os
import sys
import time
import signal
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class SnakeGameRestartHandler(FileSystemEventHandler):
    """Handler for restarting snake.py on file changes"""

    def __init__(self, script_path):
        self.script_path = script_path
        self.process = None
        self.start_game()

    def start_game(self):
        """Start or restart the snake game"""
        if self.process:
            print("\n" + "="*60)
            print("Stopping current game...")
            print("="*60)
            try:
                self.process.terminate()
                self.process.wait(timeout=2)
            except subprocess.TimeoutExpired:
                self.process.kill()
                self.process.wait()

        print("\n" + "="*60)
        print("Starting Snake Game")
        print("="*60 + "\n")

        self.process = subprocess.Popen(
            [sys.executable, self.script_path],
            cwd=os.path.dirname(os.path.abspath(self.script_path))
        )

    def on_modified(self, event):
        """Called when snake.py is modified"""
        if event.src_path.endswith('snake.py') and not event.is_directory:
            print("\n" + "="*60)
            print("File changed: snake.py")
            print("="*60)
            time.sleep(0.5)  # Brief delay to ensure file write is complete
            self.start_game()

    def cleanup(self):
        """Clean up running process"""
        if self.process:
            try:
                self.process.terminate()
                self.process.wait(timeout=2)
            except subprocess.TimeoutExpired:
                self.process.kill()
                self.process.wait()

def main():
    """Main entry point"""
    script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'snake.py')

    if not os.path.exists(script_path):
        print(f"ERROR: snake.py not found at {script_path}")
        sys.exit(1)

    print("="*60)
    print("Snake Game Terminal Watcher")
    print("="*60)
    print(f"Watching: {script_path}")
    print("Press Ctrl+C to stop")
    print("="*60)

    # Create handler and observer
    handler = SnakeGameRestartHandler(script_path)
    observer = Observer()
    observer.schedule(handler, os.path.dirname(script_path), recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\nShutting down...")
        observer.stop()
        handler.cleanup()

    observer.join()
    print("Watcher stopped.")

if __name__ == '__main__':
    try:
        main()
    except ImportError:
        print("\nERROR: Required packages not installed!")
        print("\nPlease install required packages:")
        print("  pip3 install watchdog")
        print()
        print("Then run this script again.")
        sys.exit(1)

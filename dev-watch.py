#!/usr/bin/env python3
"""
Development File Watcher with Auto-Restart
===========================================

Uses watchdog to monitor file changes and automatically restart the Python HTTP server.

Installation:
    pip3 install watchdog

Usage:
    python3 dev-watch.py

Features:
- Monitors all Python, HTML, CSS, and JS files
- Automatically restarts server on file changes
- Color-coded console output
- Graceful shutdown and restart
- Runs on http://0.0.0.0:8000
"""

import os
import sys
import time
import signal
import subprocess
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# ANSI color codes
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

class ServerRestartHandler(FileSystemEventHandler):
    """Handler for file system events that triggers server restart"""

    def __init__(self, server_manager):
        self.server_manager = server_manager
        self.last_restart = 0
        self.restart_delay = 1  # Minimum seconds between restarts

    def on_modified(self, event):
        """Called when a file is modified"""
        if event.is_directory:
            return

        # Filter file types we care about
        if not any(event.src_path.endswith(ext) for ext in ['.py', '.html', '.css', '.js']):
            return

        # Avoid too frequent restarts
        current_time = time.time()
        if current_time - self.last_restart < self.restart_delay:
            return

        self.last_restart = current_time

        # Get relative path for display
        rel_path = os.path.relpath(event.src_path)
        timestamp = datetime.now().strftime("%H:%M:%S")

        print(f"{Colors.OKCYAN}[{timestamp}]{Colors.ENDC} File changed: {Colors.WARNING}{rel_path}{Colors.ENDC}")
        self.server_manager.restart_server()

class ServerManager:
    """Manages the HTTP server process"""

    def __init__(self, port=8000):
        self.port = port
        self.process = None
        self.base_dir = os.path.dirname(os.path.abspath(__file__))

    def start_server(self):
        """Start the HTTP server"""
        if self.process:
            self.stop_server()

        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"{Colors.OKGREEN}[{timestamp}]{Colors.ENDC} Starting server on port {self.port}...")

        try:
            # Start Python HTTP server
            self.process = subprocess.Popen(
                [sys.executable, '-m', 'http.server', str(self.port), '--bind', '0.0.0.0'],
                cwd=self.base_dir,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            print(f"{Colors.OKGREEN}[{timestamp}]{Colors.ENDC} Server started at http://0.0.0.0:{self.port}")
        except Exception as e:
            print(f"{Colors.FAIL}[{timestamp}]{Colors.ENDC} Error starting server: {e}")

    def stop_server(self):
        """Stop the HTTP server"""
        if self.process:
            timestamp = datetime.now().strftime("%H:%M:%S")
            print(f"{Colors.WARNING}[{timestamp}]{Colors.ENDC} Stopping server...")

            try:
                self.process.terminate()
                self.process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                self.process.kill()

            self.process = None

    def restart_server(self):
        """Restart the HTTP server"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"{Colors.OKBLUE}[{timestamp}]{Colors.ENDC} Restarting server...")
        self.start_server()

def main():
    """Main entry point"""
    print("=" * 70)
    print(f"{Colors.HEADER}{Colors.BOLD}Development File Watcher with Auto-Restart{Colors.ENDC}")
    print("=" * 70)

    base_dir = os.path.dirname(os.path.abspath(__file__))
    port = 8000

    print(f"Server URL:      http://0.0.0.0:{port}")
    print(f"Watching:        {base_dir}")
    print(f"File types:      .py, .html, .css, .js")
    print()
    print(f"{Colors.OKGREEN}Press Ctrl+C to stop{Colors.ENDC}")
    print("=" * 70)
    print()

    # Create server manager
    server_manager = ServerManager(port=port)
    server_manager.start_server()

    # Create file watcher
    event_handler = ServerRestartHandler(server_manager)
    observer = Observer()
    observer.schedule(event_handler, base_dir, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print(f"\n{Colors.WARNING}Shutting down...{Colors.ENDC}")
        observer.stop()
        server_manager.stop_server()

    observer.join()
    print(f"{Colors.OKGREEN}Server stopped.{Colors.ENDC}")

if __name__ == '__main__':
    try:
        main()
    except ImportError as e:
        print(f"\n{Colors.FAIL}ERROR: Required packages not installed!{Colors.ENDC}")
        print("\nPlease install required packages:")
        print("  pip3 install watchdog")
        print()
        print("Then run this script again.")
        sys.exit(1)

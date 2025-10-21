#!/bin/bash
################################################################################
# Development Server Launcher
################################################################################
#
# Quick launcher for Python development servers with auto-reload.
# Choose the best server for your needs!
#
################################################################################

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Function to print colored messages
print_header() {
    echo -e "${CYAN}========================================================================${NC}"
    echo -e "${CYAN}$1${NC}"
    echo -e "${CYAN}========================================================================${NC}"
}

print_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

print_error() {
    echo -e "${RED}✗ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠ $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ $1${NC}"
}

# Check if Python is installed
check_python() {
    if ! command -v python3 &> /dev/null; then
        print_error "Python 3 is not installed!"
        exit 1
    fi
    print_success "Python 3 found: $(python3 --version)"
}

# Install dependencies
install_deps() {
    print_header "Installing Python Dependencies"

    if [ -f "requirements-dev.txt" ]; then
        print_info "Installing from requirements-dev.txt..."
        pip3 install -r requirements-dev.txt
    else
        print_info "Installing individual packages..."
        pip3 install flask flask-cors livereload watchdog fastapi uvicorn[standard]
    fi

    print_success "Dependencies installed!"
}

# Show menu
show_menu() {
    clear
    print_header "Python Development Server Launcher"
    echo ""
    echo -e "${GREEN}Choose a development server:${NC}"
    echo ""
    echo -e "  ${YELLOW}1)${NC} Flask (Basic Auto-Reload)"
    echo -e "     - Auto-reload on Python changes"
    echo -e "     - Simple and reliable"
    echo -e "     - Good for: Backend development"
    echo ""
    echo -e "  ${YELLOW}2)${NC} Flask + LiveReload ${GREEN}[RECOMMENDED]${NC}"
    echo -e "     - Auto-reload on ALL file changes (HTML/CSS/JS/Python)"
    echo -e "     - Automatic browser refresh"
    echo -e "     - Good for: Frontend development"
    echo ""
    echo -e "  ${YELLOW}3)${NC} Watchdog + HTTP Server"
    echo -e "     - File watcher with auto-restart"
    echo -e "     - Color-coded console output"
    echo -e "     - Good for: Simple static serving with monitoring"
    echo ""
    echo -e "  ${YELLOW}4)${NC} FastAPI + Uvicorn"
    echo -e "     - Ultra-fast ASGI server"
    echo -e "     - Auto-reload on Python changes"
    echo -e "     - Good for: API development"
    echo ""
    echo -e "  ${YELLOW}5)${NC} Install/Update Dependencies"
    echo -e "  ${YELLOW}6)${NC} Snake Game Terminal Watch (auto-restart snake.py)"
    echo -e "  ${YELLOW}0)${NC} Exit"
    echo ""
}

# Launch Flask basic
launch_flask() {
    print_header "Starting Flask Development Server"
    python3 dev-server-flask.py
}

# Launch Flask + LiveReload
launch_livereload() {
    print_header "Starting Flask + LiveReload Server"
    python3 dev-server-livereload.py
}

# Launch Watchdog
launch_watchdog() {
    print_header "Starting Watchdog File Watcher"
    python3 dev-watch.py
}

# Launch FastAPI
launch_fastapi() {
    print_header "Starting FastAPI Development Server"
    python3 dev-fastapi.py
}

# Launch Snake game watcher
launch_snake_watch() {
    print_header "Starting Snake Game Terminal Watcher"

    # Check if entr is available
    if command -v entr &> /dev/null; then
        print_success "Using 'entr' for file watching"
        print_info "Playing snake.py - will auto-restart on changes"
        echo ""
        echo "snake.py" | entr -r python3 snake.py
    elif [ -f "dev-snake-watch.py" ]; then
        print_success "Using Python watchdog for file watching"
        python3 dev-snake-watch.py
    else
        print_warning "Installing watchdog for file watching..."
        pip3 install watchdog
        python3 -c "
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import sys
import time

class SnakeRestartHandler(FileSystemEventHandler):
    def __init__(self):
        self.process = None
        self.start_game()

    def start_game(self):
        if self.process:
            self.process.terminate()
            self.process.wait()
        print('\n=== Starting Snake Game ===\n')
        self.process = subprocess.Popen([sys.executable, 'snake.py'])

    def on_modified(self, event):
        if event.src_path.endswith('snake.py'):
            print('\n=== Restarting Snake Game ===\n')
            self.start_game()

handler = SnakeRestartHandler()
observer = Observer()
observer.schedule(handler, '.', recursive=False)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
    if handler.process:
        handler.process.terminate()

observer.join()
"
    fi
}

# Main script
main() {
    check_python

    while true; do
        show_menu

        read -p "Enter your choice [0-6]: " choice

        case $choice in
            1)
                launch_flask
                ;;
            2)
                launch_livereload
                ;;
            3)
                launch_watchdog
                ;;
            4)
                launch_fastapi
                ;;
            5)
                install_deps
                echo ""
                read -p "Press Enter to continue..."
                ;;
            6)
                launch_snake_watch
                ;;
            0)
                print_info "Goodbye!"
                exit 0
                ;;
            *)
                print_error "Invalid choice. Please try again."
                sleep 2
                ;;
        esac
    done
}

# Run main script
main

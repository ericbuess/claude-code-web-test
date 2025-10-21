#!/usr/bin/env python3
"""
Quick Server Test Script
========================

Tests that all development servers can be imported successfully.
"""

import sys

def test_imports():
    """Test that all required modules can be imported"""
    results = {}

    # Test Flask
    try:
        import flask
        from flask_cors import CORS
        results['Flask'] = f'✓ Installed (v{flask.__version__})'
    except ImportError as e:
        results['Flask'] = f'✗ Not installed: {e}'

    # Test LiveReload
    try:
        import livereload
        results['LiveReload'] = '✓ Installed'
    except ImportError as e:
        results['LiveReload'] = f'✗ Not installed: {e}'

    # Test Watchdog
    try:
        import watchdog
        results['Watchdog'] = '✓ Installed'
    except ImportError as e:
        results['Watchdog'] = f'✗ Not installed: {e}'

    # Test FastAPI
    try:
        import fastapi
        import uvicorn
        results['FastAPI'] = '✓ Installed'
    except ImportError as e:
        results['FastAPI'] = f'✗ Not installed: {e}'

    return results

def test_server_files():
    """Test that all server files exist"""
    import os
    base_dir = os.path.dirname(os.path.abspath(__file__))

    files = {
        'dev-server-flask.py': 'Flask Basic Server',
        'dev-server-livereload.py': 'Flask LiveReload Server',
        'dev-watch.py': 'Watchdog File Watcher',
        'dev-fastapi.py': 'FastAPI Server',
        'dev-snake-watch.py': 'Snake Game Watcher',
        'start-dev.sh': 'Interactive Launcher'
    }

    results = {}
    for filename, description in files.items():
        filepath = os.path.join(base_dir, filename)
        if os.path.exists(filepath):
            results[description] = '✓ File exists'
        else:
            results[description] = '✗ File missing'

    return results

if __name__ == '__main__':
    print("=" * 70)
    print("Development Server Test")
    print("=" * 70)

    print("\n📦 Dependency Check:")
    print("-" * 70)
    for name, status in test_imports().items():
        print(f"  {name:20} {status}")

    print("\n📄 Server Files Check:")
    print("-" * 70)
    for name, status in test_server_files().items():
        print(f"  {name:30} {status}")

    print("\n" + "=" * 70)
    print("Test complete!")
    print("=" * 70)

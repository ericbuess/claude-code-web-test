"""
Test Playwright - requires Playwright browsers installed
"""
from playwright.sync_api import sync_playwright
import time

def test_playwright():
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            
            page.goto('http://localhost:8000/snake.html')
            time.sleep(2)
            
            page.screenshot(path='/tmp/snake_playwright.png')
            print("Playwright screenshot saved successfully!")
            
            browser.close()
            return True
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    test_playwright()

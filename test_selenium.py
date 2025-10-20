"""
Test Selenium with Chrome - requires Chrome browser
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

def test_selenium_chrome():
    try:
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        
        service = Service()
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        driver.get('http://localhost:8000/snake.html')
        time.sleep(2)
        
        driver.save_screenshot('/tmp/snake_screenshot.png')
        print("Screenshot saved successfully!")
        
        driver.quit()
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    test_selenium_chrome()

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
import sys

def get_final_url(initial_url):
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    try:
        driver.get(initial_url)
        # Give it a few seconds to handle redirects/javascript
        import time
        time.sleep(5) 
        
        # Return the current URL (the one it redirected to)
        return driver.current_url
    finally:
        driver.quit()

if __name__ == "__main__":
    url = os.environ.get("URL")
    print(get_final_url(url))

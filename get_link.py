from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
import time

def get_download_url():
    url = os.environ.get("URL")
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    # Standard User-Agent to avoid bots detection
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    try:
        driver.get(url)
        # Wait for the automatic redirect/link generation to happen
        time.sleep(10) 
        
        # This returns the URL the browser is currently looking at
        # If the page "auto-downloads", the URL often changes to the file link
        print(driver.current_url)
    finally:
        driver.quit()

if __name__ == "__main__":
    get_download_url()

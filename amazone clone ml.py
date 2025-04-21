from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import os

def setup_driver():
    options = Options()
    options.add_argument("--headless")  # Run without GUI
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    
    # Modify this line with the correct path to your ChromeDriver
    service = Service("C:\chromedriver-win64\chromedriver.exe")  # Update this path
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def clone_amazon_page(url, output_folder):
    driver = setup_driver()
    driver.get(url)
    time.sleep(5)  # Allow dynamic content to load

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    html_file = os.path.join(output_folder, 'amazon.html')
    with open(html_file, 'w', encoding='utf-8') as file:
        file.write(str(soup))

    print(f"Amazon page cloned successfully: {html_file}")

# Example usage:
clone_amazon_page("https://www.amazon.com", "cloned_amazon")

import sys
import time
import datetime
import argparse
import threading
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import InvalidArgumentException, WebDriverException, TimeoutException
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

# Argument parser for browser and URL input
parser = argparse.ArgumentParser(description='Run Selenium WebDriver with specified browser.')
parser.add_argument('-b', '--browser', choices=['Edge', 'edge', 'Firefox', 'firefox', 'Chrome', 'chrome'], required=True, help='Specify the browser to use.')
parser.add_argument('-u', '--url', required=True, help='Input the YouTube Channel URL.')
args = parser.parse_args()

def init_driver(browser):
    if browser.lower() == 'edge':
        options = webdriver.EdgeOptions()
        options.add_argument('--headless')
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
    elif browser.lower() == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    elif browser.lower() == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    else:
        raise ValueError("Unsupported browser")
    return driver

def scroll_page(driver, scroll_complete_event):
    last_height = driver.execute_script("return document.documentElement.scrollHeight")
    while not scroll_complete_event.is_set():
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        time.sleep(2)  # Adjust sleep time as needed
        new_height = driver.execute_script("return document.documentElement.scrollHeight")
        if new_height == last_height:
            scroll_complete_event.set()
        last_height = new_height

def extract_links(driver, channelid, dt, scroll_complete_event):
    links = set()  # Use a set to avoid duplicate links
    with open(channelid + '-' + dt + '.list', 'a+') as f:
        while not scroll_complete_event.is_set() or driver.find_elements(By.XPATH, '//*[@id="thumbnail"]'):
            user_data = driver.find_elements(By.XPATH, '//*[@id="thumbnail"]')
            for i in user_data:
                link = i.get_attribute('href')
                if link and link not in links:
                    links.add(link)
                    f.write(link + '\n')
            time.sleep(1)  # Adjust sleep time as needed

def main():
    driver = init_driver(args.browser)
    url = args.url.lower()
    if '@' in url:
        channelid = url.split('/')[3][1:]
    else:
        channelid = url.split('/')[4]

    dt = datetime.datetime.now().strftime("%Y%m%d%H%M")

    scroll_complete_event = threading.Event()

    driver.get(url)
    time.sleep(5)  # Wait for the page to load

    scroll_thread = threading.Thread(target=scroll_page, args=(driver, scroll_complete_event))
    extract_thread = threading.Thread(target=extract_links, args=(driver, channelid, dt, scroll_complete_event))

    scroll_thread.start()
    extract_thread.start()

    scroll_thread.join()
    extract_thread.join()

    driver.quit()

if __name__ == '__main__':
    main()

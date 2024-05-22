from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def scrape_hackathon_page(hackathon_link):
    # Set up Chrome options to run in headless mode
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Initialize Chrome browser using Selenium Manager to handle the driver
    driver = webdriver.Chrome(options=chrome_options)

    # Log into devpost
    

    # Navigate to the hackathon link
    driver.get(hackathon_link)

    # Wait for the page to load completely
    time.sleep(2)

    # Click on the element
    element = driver.find_element(By.XPATH, '//*[@id="challenge-navigation"]/div/div/nav/section/ul/li[3]/a')
    element.click()

    # Example: Extract the title of the page
    page_title = driver.title

    # Close the browser
    # driver.quit()

    return page_title

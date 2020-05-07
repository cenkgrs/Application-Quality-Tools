from selenium import webdriver
import time
import logging as L

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

log_file = "logs.txt"
pass_message = "Succesfully completed - Number"
fail_message = "Failed - Number"
timeout = 5

def logging():
    L.basicConfig(level=L.DEBUG)
    L.debug('Debug message')
    L.info("Info message")
    L.warning("Warning message")
    L.error("Error message")
    L.critical("Critical message")


def log(level, message, file):
    L.basicConfig(level=L.INFO, filename=file, filemode="w",
                  format="%(asctime)-12s %(levelname)s %(message)s",
                  datefmt="'%d-%m-%Y%H:%M:%S'")
    if level == "INFO":L.info(message)
    if level == "WARNING":L.warning(message)
    if level == "ERROR":L.error(message)
    if level == "CRITICAL":L.critical(message)


def youtube_search():

    driver = webdriver.Firefox()
    driver.get("https://www.google.com/")
    log("INFO", pass_message, log_file)

    # Search youtube in google
    driver.find_element(By.NAME, "q").send_keys("Youtube" + Keys.RETURN)
    log("INFO", pass_message, log_file)

    time.sleep(3)
    assert "No results found." not in driver.page_source
    # Select the first result link
    driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[9]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div[1]/a/h3').click()
    log("INFO", pass_message, log_file)

    # Search
    try:
        element_present = EC.visibility_of_element_located((By.NAME, 'search_query'))
        WebDriverWait(driver, timeout).until(element_present)
        driver.find_element(By.NAME, "search_query").send_keys("batman" + Keys.RETURN)
        log("INFO", pass_message, log_file)
    except TimeoutException:
        log("WARNING", "Timed out waiting for page to load", log_file)

    # Search button
    search_button = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
    search_button.click()
    log("INFO", pass_message, log_file)

    # # Select video

    element_present = EC.visibility_of_element_located((By.XPATH, '//*[@id="video-title"]'))
    WebDriverWait(driver, timeout).until(element_present)
    driver.find_element_by_xpath('//*[@id="video-title"]').click()
    log("INFO", pass_message, log_file)


youtube_search()



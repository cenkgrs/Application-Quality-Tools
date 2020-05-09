from selenium import webdriver
import time
import logging as L

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

log_file = "logs.txt"
pass_message = "Succesfully completed"
fail_message = "Failed - Number"
timeout = 5

def logging():
    L.basicConfig(level=L.DEBUG)
    L.debug('Debug message')
    L.info("Info message")
    L.warning("Warning message")
    L.error("Error message")
    L.critical("Critical message")


def log(level, action, message, file):
    message = message + " " + action
    L.basicConfig(level=L.INFO, filename=file, filemode="w",
                  format="%(asctime)-12s %(levelname)s %(message)s")

    if level == "INFO":L.info(message)
    if level == "WARNING":L.warning(message)
    if level == "ERROR":L.error(message)
    if level == "CRITICAL":L.critical(message)


def youtube_search():

    action = "Google opened"
    driver = webdriver.Firefox()
    driver.get("https://www.google.com/")
    log("INFO", action, pass_message, log_file)

    # Search youtube in google
    action = "Search youtube"
    driver.find_element(By.NAME, "q").send_keys("Youtube" + Keys.RETURN)
    log("INFO", action, pass_message, log_file)

    time.sleep(3)
    assert "No results found." not in driver.page_source
    # Select the first result link
    action = "open youtube link"
    driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[9]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div[1]/a/h3').click()
    log("INFO", action, pass_message, log_file)

    # Search
    action = "Search on youtube"
    try:
        element_present = EC.visibility_of_element_located((By.NAME, 'search_query'))
        WebDriverWait(driver, timeout).until(element_present)
        driver.find_element(By.NAME, "search_query").send_keys("batman" + Keys.RETURN)
        log("INFO",action, pass_message, log_file)
    except TimeoutException:
        log("WARNING", action, "Timed out waiting for page to load", log_file)
        return read_file()

    # Search button
    search_button = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
    search_button.click()
    log("INFO", action, pass_message, log_file)

    # # Select video
    action = "Youtube video opened"
    element_present = EC.visibility_of_element_located((By.XPATH, '//*[@id="video-title"]'))
    WebDriverWait(driver, timeout).until(element_present)
    driver.find_element_by_xpath('//*[@id="video-title"]').click()
    log("INFO", action, pass_message, log_file)

    return read_file()


def read_file():
    lines = []
    with open('logs.txt') as my_file:
        lines = my_file.readlines()
        new_lines = []
        for line in lines:

            new_line = str(line.replace(" - Number", ""))
            new_lines.append(new_line)

    return new_lines


read_file()
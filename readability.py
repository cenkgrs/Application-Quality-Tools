from bs4 import BeautifulSoup
import requests
import lxml
import selenium
from selenium import webdriver
import time


def get_readability(url):
    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data, 'lxml')
    td = []
    td = soup.find_all("td", attrs={'class': None})

    result = soup.find("p", attrs={'class': "flush-top small-copy"})
    result = result.getText()

    readability = []
    readability.append(result)

    for i in td:

        if i.string is not None:
            readability.append(str(i.string))

    return readability


def get_read(url):
    # Open the website
    driver = webdriver.Firefox()
    driver.get('https://www.webfx.com/tools/read-able/')

    input = driver.find_element_by_id('uri')
    input.send_keys('')
    time.sleep(2)
    # Write site url to input
    input.send_keys(url)
    time.sleep(2)

    # Click to send button
    button = driver.find_element_by_xpath('//*[@id="tabs-1"]/form/fieldset/div/input[2]')
    button.click()

    url = driver.current_url

    driver.close()

    # Send opened page to get_readability function
    readability = get_readability(url)

    return readability

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

    readability = {
        "result" : result.getText(),
        "Flesch Kincaid Reading Ease": td[0].string,
        "Flesch Kincaid Grade Level	": td[1].string,
        "Gunning Fog Score": td[3].string,
        "SMOG Index": td[4].string,
        "Coleman Liau Index": td[5].string,
        "Automated Readability Index": td[6].string,
        "No. of sentences": td[7].string,
        "No. of words": td[8].string,
        "No. of complex words": td[9].string,
        "Average words  per sentence": td[10].string,
        "Average syllables per word": td[11].string
    }

    return readability


def get_read():
    # Open the website
    driver = webdriver.Firefox()
    driver.get('https://www.webfx.com/tools/read-able/')

    input = driver.find_element_by_id('uri')
    input.send_keys('')
    time.sleep(2)
    input.send_keys("cenkgurses.website")
    time.sleep(2)

    button = driver.find_element_by_xpath('//*[@id="tabs-1"]/form/fieldset/div/input[2]')
    button.click()

    url = driver.current_url

    driver.close()
    readability = get_readability(url)

    return readability

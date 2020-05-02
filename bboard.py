#Sources: https://www.freecodecamp.org/news/better-web-scraping-in-python-with-selenium-beautiful-soup-and-pandas-d6390592e251/
#https://www.kenst.com/2015/03/including-the-chromedriver-location-in-macos-system-path/

#pip3 install -U selenium
# pip3 install chromedriver_installer
# pip3 install BeautifulSoup4
# pip3 install lxml

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from bs4 import BeautifulSoup
import requests
import pandas as pd
import time


#async def getBlackboardInfo(username, password):
def getBlackboardInfo(username, password):
    EMAIL = username
    PASSWORD = password

    url = "https://uic.blackboard.com/?new_loc=%2Fultra%2Finstitution-page%2Feffective"

    #driver = webdriver.Chrome()
    driver = webdriver.Remote(command_executor='http://hub:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)


    driver.implicitly_wait(30)
    driver.get(url)

    loginButton = driver.find_element_by_xpath('/html/body/div[1]/section/div[1]/div/div/div[1]/a')
    actions = ActionChains(driver)
    actions.move_to_element(loginButton)
    actions.click(loginButton)
    actions.perform()

   
    usrname = driver.find_element_by_xpath('/html/body/div[2]/form/input[8]')
    usrname.send_keys(EMAIL)

    pword = driver.find_element_by_xpath('/html/body/div[2]/form/input[9]')
    pword.send_keys(PASSWORD)

    pword.send_keys(Keys.RETURN)

    driver.get('https://uic.blackboard.com/ultra/stream')

    time.sleep(4)
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    streams = soup.find(id="activity-stream").findAll('div', recursive=False)
    notes = streams[0].find('h2')
    for stream in streams:
        if stream.find('h2').text == "Recent":
            notes = stream

    info = []
    for note in notes.findAll('div'):
        info.append(note.text)

    blackboardInfo = []
    #learned how to filter out empty strings from geeksforgeeks.org
    for item in info:
        note = {}
        note["content"] = list(filter(None, item.strip().splitlines()))
        if(len(note["content"]) > 2):
            blackboardInfo.append(note)
    
    driver.quit()

    #print(blackboardInfo)

    return blackboardInfo
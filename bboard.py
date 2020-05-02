#Sources: https://www.freecodecamp.org/news/better-web-scraping-in-python-with-selenium-beautiful-soup-and-pandas-d6390592e251/
#https://www.kenst.com/2015/03/including-the-chromedriver-location-in-macos-system-path/

# some of the pip packages we had to install:
#   pip3 install -U selenium
#   pip3 install chromedriver_installer
#   pip3 install BeautifulSoup4
#   pip3 install lxml

# import all of our libraries
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

# function that gets us the information we need from gradescope
def getBlackboardInfo(username, password):

    # set our username/email variable
    EMAIL = username
    # set our password variable
    PASSWORD = password

    # set our blackboard url
    url = "https://uic.blackboard.com/?new_loc=%2Fultra%2Finstitution-page%2Feffective"

    # we will need a web scraper to do this, since there is no API
    # the scraper we are using is selenium

    # our web driver, this is like our 'browser'
    # we have a selenium hub docker image running
    # it has multiple 'chrome' nodes
    # this web driver will connect to one of those 'chrome' nodes
    driver = webdriver.Remote(command_executor='http://hub:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)

    # in case it takes a while, set our max waiting times
    driver.implicitly_wait(30)
    # fetch the blackboard site
    driver.get(url)

    # find the login button on the page
    loginButton = driver.find_element_by_xpath('/html/body/div[1]/section/div[1]/div/div/div[1]/a')

    # click the login button
    actions = ActionChains(driver)
    actions.move_to_element(loginButton)
    actions.click(loginButton)
    actions.perform()

    # find the username field and fill it in
    usrname = driver.find_element_by_xpath('/html/body/div[2]/form/input[8]')
    usrname.send_keys(EMAIL)

    # find the password field and fill it in
    pword = driver.find_element_by_xpath('/html/body/div[2]/form/input[9]')
    pword.send_keys(PASSWORD)

    # send enter, to basically attempt to login
    pword.send_keys(Keys.RETURN)

    # now navigate to our stream
    driver.get('https://uic.blackboard.com/ultra/stream')

    # this can be incredibly slow
    # so use a hard sleep to wait for it to load
    time.sleep(4)
    
     # we will use beautiful soup to parse the webpage that we receive
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # find our streams
    streams = soup.find(id="activity-stream").findAll('div', recursive=False)

    # get the stream that we want, which is the 'Recent' stream
    # we use this stream because it basically has everything
    notes = streams[0].find('h2')
    for stream in streams:
        if stream.find('h2').text == "Recent":
            notes = stream

    # store each bit of stream info here
    info = []
    for note in notes.findAll('div'):
        info.append(note.text)

    # store all our stream infos as a list here
    blackboardInfo = []
    #learned how to filter out empty strings from geeksforgeeks.org
    for item in info:
        note = {}
        # clean out empty strings and spaces
        # because data is messy, and empty strings occur frequently
        note["content"] = list(filter(None, item.strip().splitlines()))
        if(len(note["content"]) > 2):
            blackboardInfo.append(note)
    
    # make sure to quit our driver
    driver.quit()

    # return our info
    return blackboardInfo
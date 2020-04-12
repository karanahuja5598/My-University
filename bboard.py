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
from bs4 import BeautifulSoup
import requests
import pandas as pd





EMAIL = ""
PASSWORD = ""
currentSem = "Spring 2020"

url = "https://uic.blackboard.com/?new_loc=%2Fultra%2Finstitution-page%2Feffective"

def main():
    driver = webdriver.Chrome()


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
    
    #soup = BeautifulSoup(driver.page_source, 'html.parser')
  
    

    #upcoming = driver.find_element_by_xpath('/html/body/div[1]/div[2]/bb-base-layout/div/main/div/div/div[1]/div[1]/div/div/div[1]').text


    stream = driver.find_element_by_xpath('/html/body/div[1]/div[2]/bb-base-layout/div/main/div/div/div[1]/div[1]/div/div/div[3]').text


    print(stream)

    
    #curUpcoming = upcoming.find('div')
    #print(curUpcoming)
    """
    courseList = curSemCourses.findAll('a')
    courseLinks = []
    for i in courseList:
        courseLinks.append(url[:-1] + i.get('href'))
    
    frames = []
    for x in courseLinks:
        driver.get(x)
        soup1 = BeautifulSoup(driver.page_source, 'html.parser')
        tbl = soup1.find('table',{"id":"assignments-student-table"})
        frames.append(pd.read_html(str(tbl))[0])
    
    print(frames)

    #logUsrPass = driver.find_element_by_xpath('/html/body/div[1]/dialog/div/div[1]/form/div[4]/input')
    #logUsrPass = driver.find_element_by_name('commit')
    #logUsrPass = driver.find_element_by_xpath("//input[type='submit']")
    #logUsrPass = driver.find_element_by_name('Log Inss')
    #actions.move_to_element(logUsrPass)
    #actions.click(logUsrPass)
    #actions.perform()

    #elems = driver.find_elements_by_xpath("//a[@href]")
    #for elem in elems:
        #print(elem.get_attribute("href"))
    
`"""
    driver.quit()

if __name__ == '__main__':
    main()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from bs4 import BeautifulSoup
import requests
import pandas as pd
import time





EMAIL = ""
PASSWORD = ""
currentSem = "Spring 2020"

url = "https://uic.blackboard.com/?new_loc=%2Fultra%2Finstitution-page%2Feffective"

def main():
    #log in info for piazza
        
        EMAIL = "usert4363@gmail.com"
        PASSWORD = "cs494Awesome"

        # first, we'll register to the app

        url = "http://localhost:5000/register"

        driver = webdriver.Chrome()

        driver.implicitly_wait(30)
        driver.get(url)
        
        usrname = driver.find_element_by_xpath('/html/body/form/p[1]/input')
        usrname.send_keys("j")

        pword = driver.find_element_by_xpath('/html/body/form/p[2]/input')
        pword.send_keys("j")

        pword.send_keys(Keys.RETURN)

        # next we'll login

        url = "http://localhost:5000/login"

        driver.get(url)
        
        usrname = driver.find_element_by_xpath('/html/body/form/p[1]/input')
        usrname.send_keys("j")

        pword = driver.find_element_by_xpath('/html/body/form/p[2]/input')
        pword.send_keys("j")

        pword.send_keys(Keys.RETURN)

        # next we'll update piazza information

        url = "http://localhost:5000/registerGradescope"

        driver.get(url)
        
        usrname = driver.find_element_by_xpath('/html/body/form/p[1]/input')
        usrname.send_keys(EMAIL)

        pword = driver.find_element_by_xpath('/html/body/form/p[2]/input')
        pword.send_keys(PASSWORD)

        pword.send_keys(Keys.RETURN)

        # next we'll load our piazza information

        url = "http://localhost:5000/gradescope"

        #wait = WebDriverWait(driver, 60)

        driver.get(url)

        #first_result = wait.until(presence_of_element_located((By.CSS_SELECTOR, "h3>div")))

        soup = BeautifulSoup(driver.page_source, 'html.parser')

        testText = soup.find('h3').text

        print(testText)

        driver.quit()

if __name__ == '__main__':
    main()
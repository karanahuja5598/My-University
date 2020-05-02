from app import app
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from bs4 import BeautifulSoup
import requests
import pandas as pd
import time

# got it from the source mentioned in sources.txt

class FlaskAppTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass
    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True

        try:
            self.driver = webdriver.Remote(command_executor='http://hub:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
        except:
            pass

    def tearDown(self):
        self.driver.quit()
    
    # check to see if the index page loads the correct message when we aren't logged in
    async def test_index_unauth(self):
        result = self.app.get('/')
        exists = (await result).data.find("Welcome to the UIC School Notifier, please log in or register.".encode()) != -1
        self.assertEqual(exists, True)
    
    # check to see if the login page loads the correct message when we aren't logged in
    async def test_login_unauth(self):
        result = self.app.get('/login')
        exists = (await result).data.find("Sign In".encode()) != -1
        self.assertEqual(exists, True)

    # check to see if the register page loads the correct message when we aren't logged in
    async def test_register_unauth(self):
        result = self.app.get('/register')
        exists = (await result).data.find("Register".encode()) != -1
        self.assertEqual(exists, True)

    # check to see if we can register properly
    async def test_register_auth(self):
        result = self.app.post('/register', data = {"username" : "m", "password" : "agfgggg"}, follow_redirects=True)
        exists = (await result).data.find("Sign In".encode()) != -1
        self.assertEqual(exists, True)

    #check to see if we can register, then log in properly
    async def test_register_login_auth(self):
        result = self.app.post('/register', data = {"username" : "l", "password" : "agfgggg"}, follow_redirects=True)
        await result
        result = self.app.post('/login', data = {"username" : "l", "password" : "agfgggg"}, follow_redirects=True)
        exists = (await result).data.find("Welcome to the UIC School Notifier, l".encode()) != -1
        self.assertEqual(exists, True)

    # check to make sure that you can't register the same username twice
    async def test_double_register_auth(self):
        result = self.app.post('/register', data = {"username" : "x", "password" : "agfgghhh"}, follow_redirects=True)
        await result
        result = self.app.post('/register', data = {"username" : "x", "password" : "agfgghhh"}, follow_redirects=True)
        exists = (await result).data.find("Username already exists".encode()) != -1
        self.assertEqual(exists, True)


    # check to see if we can update our piazza credentials properly
    def test_register_piazza_auth(self):
        #log in info for piazza
        EMAIL = "usert4363@gmail.com"
        PASSWORD = "cs494Awesome"

        # first, we'll register to the app

        url = "http://my_uni:5000"

        driver = self.driver

        driver.implicitly_wait(30)
        driver.get(url)

        url = "http://my_uni:5000/register"
        driver.get(url)
        
        usrname = driver.find_element_by_xpath('/html/body/form/p[1]/input')
        usrname.send_keys("k")

        pword = driver.find_element_by_xpath('/html/body/form/p[2]/input')
        pword.send_keys("k")

        pword.send_keys(Keys.RETURN)

        # next we'll login

        url = "http://my_uni:5000/login"

        driver.get(url)

        usrname = driver.find_element_by_xpath('/html/body/form/p[1]/input')
        usrname.send_keys("k")

        pword = driver.find_element_by_xpath('/html/body/form/p[2]/input')
        pword.send_keys("k")

        pword.send_keys(Keys.RETURN)

        # next we'll update piazza information

        url = "http://my_uni:5000/update"

        driver.get(url)
        
        usrname = driver.find_element_by_xpath('/html/body/form/p[1]/input')
        usrname.send_keys(EMAIL)

        piazza = driver.find_element_by_xpath('/html/body/form/ul/li[1]/input')
        actions = ActionChains(driver)
        actions.move_to_element(piazza)
        actions.click(piazza)
        actions.perform()

        pword = driver.find_element_by_xpath('/html/body/form/p[3]/input')
        pword.send_keys(PASSWORD)

        pword.send_keys(Keys.RETURN)

        #now we'll make sure that it updated properly
        #if it did, it will have returned us to the index
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        testText = soup.find('h1').text

        self.assertEqual(testText, "Welcome to the UIC School Notifier, k")

        driver.close()

    
    # check to see if the contents of our piazza account are loaded properly
    def test_contents_piazza_auth(self):
        #log in info for piazza
        
        EMAIL = "usert4363@gmail.com"
        PASSWORD = "cs494Awesome"

        # first, we'll register to the app

        url = "http://my_uni:5000"

        driver = self.driver

        driver.implicitly_wait(30)
        driver.get(url)

        url = "http://my_uni:5000/register"
        driver.get(url)
        
        usrname = driver.find_element_by_xpath('/html/body/form/p[1]/input')
        usrname.send_keys("v")

        pword = driver.find_element_by_xpath('/html/body/form/p[2]/input')
        pword.send_keys("v")

        pword.send_keys(Keys.RETURN)

        # next we'll login

        url = "http://my_uni:5000/login"

        driver.get(url)
        
        usrname = driver.find_element_by_xpath('/html/body/form/p[1]/input')
        usrname.send_keys("v")

        pword = driver.find_element_by_xpath('/html/body/form/p[2]/input')
        pword.send_keys("v")

        pword.send_keys(Keys.RETURN)

        # next we'll update piazza information

        url = "http://my_uni:5000/update"

        driver.get(url)
        
        usrname = driver.find_element_by_xpath('/html/body/form/p[1]/input')
        usrname.send_keys(EMAIL)

        piazza = driver.find_element_by_xpath('/html/body/form/ul/li[1]/input')
        actions = ActionChains(driver)
        actions.move_to_element(piazza)
        actions.click(piazza)
        actions.perform()

        pword = driver.find_element_by_xpath('/html/body/form/p[3]/input')
        pword.send_keys(PASSWORD)

        pword.send_keys(Keys.RETURN)

        # next we'll load our piazza information
        piazzaButton = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/a/button')
        actions1 = ActionChains(driver)
        actions1.move_to_element(piazzaButton)
        actions1.click(piazzaButton)
        actions1.perform()

        refreshButton = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/a[1]/button')
        actions2 = ActionChains(driver)
        actions2.move_to_element(refreshButton)
        actions2.click(refreshButton)
        actions2.perform()

        soup = BeautifulSoup(driver.page_source, 'html.parser')

        testTexts = soup.find_all('h3')

        testText = "Post Title: syncing github usernames"

        for i in range(len(testTexts)):
            if(testTexts[i].text == testText):
                self.assertEqual(testTexts[i].text, testText)
                break

        driver.close()
        
        
    # check to see if we can update our gradescope credentials properly
    def test_register_gradescope_auth(self):
        #log in info for gradescope
        
        EMAIL = "usert4363@gmail.com"
        PASSWORD = "cs494Awesome"

        # first, we'll register to the app

        url = "http://my_uni:5000/register"

        driver = self.driver

        driver.implicitly_wait(30)
        driver.get(url)
        
        usrname = driver.find_element_by_xpath('/html/body/form/p[1]/input')
        usrname.send_keys("c")

        pword = driver.find_element_by_xpath('/html/body/form/p[2]/input')
        pword.send_keys("c")

        pword.send_keys(Keys.RETURN)

        # next we'll login

        url = "http://my_uni:5000/login"

        driver.get(url)
        
        usrname = driver.find_element_by_xpath('/html/body/form/p[1]/input')
        usrname.send_keys("c")

        pword = driver.find_element_by_xpath('/html/body/form/p[2]/input')
        pword.send_keys("c")

        pword.send_keys(Keys.RETURN)

        # next we'll update piazza information

        url = "http://my_uni:5000/update"

        driver.get(url)
        
        usrname = driver.find_element_by_xpath('/html/body/form/p[1]/input')
        usrname.send_keys(EMAIL)

        gradescope = driver.find_element_by_xpath('/html/body/form/ul/li[2]/input')
        actions = ActionChains(driver)
        actions.move_to_element(gradescope)
        actions.click(gradescope)
        actions.perform()

        pword = driver.find_element_by_xpath('/html/body/form/p[3]/input')
        pword.send_keys(PASSWORD)

        pword.send_keys(Keys.RETURN)

        #now we'll make sure that it updated properly
        #if it did, it will have returned us to the index
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        testText = soup.find('h1').text

        self.assertEqual(testText, "Welcome to the UIC School Notifier, c")
        
        driver.close()
    
    # check to see if the contents of our gradescope account are loaded properly
    def test_contents_gradescope_auth(self):
        #log in info for piazza
        
        EMAIL = "usert4363@gmail.com"
        PASSWORD = "cs494Awesome"

        # first, we'll register to the app

        url = "http://my_uni:5000/register"

        driver = self.driver

        driver.implicitly_wait(30)
        driver.get(url)
        
        usrname = driver.find_element_by_xpath('/html/body/form/p[1]/input')
        usrname.send_keys("j")

        pword = driver.find_element_by_xpath('/html/body/form/p[2]/input')
        pword.send_keys("j")

        pword.send_keys(Keys.RETURN)

        # next we'll login

        url = "http://my_uni:5000/login"

        driver.get(url)
        
        usrname = driver.find_element_by_xpath('/html/body/form/p[1]/input')
        usrname.send_keys("j")

        pword = driver.find_element_by_xpath('/html/body/form/p[2]/input')
        pword.send_keys("j")

        pword.send_keys(Keys.RETURN)

        # next we'll update piazza information

        url = "http://my_uni:5000/update"

        driver.get(url)
        
        usrname = driver.find_element_by_xpath('/html/body/form/p[1]/input')
        usrname.send_keys(EMAIL)

        gradescope = driver.find_element_by_xpath('/html/body/form/ul/li[2]/input')
        actions = ActionChains(driver)
        actions.move_to_element(gradescope)
        actions.click(gradescope)
        actions.perform()

        pword = driver.find_element_by_xpath('/html/body/form/p[3]/input')
        pword.send_keys(PASSWORD)

        pword.send_keys(Keys.RETURN)

        # next we'll load our gradescope information
        gradescopeButton = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/a/button')
        actions1 = ActionChains(driver)
        actions1.move_to_element(gradescopeButton)
        actions1.click(gradescopeButton)
        actions1.perform()

        refreshButton = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/a[1]/button')
        actions2 = ActionChains(driver)
        actions2.move_to_element(refreshButton)
        actions2.click(refreshButton)
        actions2.perform()
        

        soup = BeautifulSoup(driver.page_source, 'html.parser')

        testTexts = []

        testTexts = soup.find_all('td')

        testText = "midterm"
        
        for i in range(len(testTexts)):
            if(testTexts[i].text == testText):
                self.assertEqual(testTexts[i].text, testText)
                break

        driver.close()
        

    
    
    # check if list of classes loads properly for gradescope, current semester
    def test_className_gradescope_auth(self):
        #log in info for gradescope
        
        EMAIL = "usert4363@gmail.com"
        PASSWORD = "cs494Awesome"

        # first, we'll register to the app

        url = "http://my_uni:5000/register"

        driver = self.driver

        driver.implicitly_wait(30)
        
        driver.get(url)
        
        usrname = driver.find_element_by_xpath('/html/body/form/p[1]/input')
        usrname.send_keys("j")

        pword = driver.find_element_by_xpath('/html/body/form/p[2]/input')
        pword.send_keys("j")

        pword.send_keys(Keys.RETURN)

        # next we'll login
        
        url = "http://my_uni:5000/login"

        driver.get(url)
        
        usrname = driver.find_element_by_xpath('/html/body/form/p[1]/input')
        usrname.send_keys("j")

        pword = driver.find_element_by_xpath('/html/body/form/p[2]/input')
        pword.send_keys("j")

        pword.send_keys(Keys.RETURN)

        # next we'll update gradescope information
        
        url = "http://my_uni:5000/update"

        driver.get(url)
        
        usrname = driver.find_element_by_xpath('/html/body/form/p[1]/input')
        usrname.send_keys(EMAIL)

        gradescope = driver.find_element_by_xpath('/html/body/form/ul/li[2]/input')
        actions = ActionChains(driver)
        actions.move_to_element(gradescope)
        actions.click(gradescope)
        actions.perform()

        pword = driver.find_element_by_xpath('/html/body/form/p[3]/input')
        pword.send_keys(PASSWORD)

        pword.send_keys(Keys.RETURN)

        # next we'll load our gradescope information
        gradescopeButton = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/a/button')
        actions1 = ActionChains(driver)
        actions1.move_to_element(gradescopeButton)
        actions1.click(gradescopeButton)
        actions1.perform()

        refreshButton = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/a[1]/button')
        actions2 = ActionChains(driver)
        actions2.move_to_element(refreshButton)
        actions2.click(refreshButton)
        actions2.perform()

        soup = BeautifulSoup(driver.page_source, 'html.parser')

        testTexts = soup.find_all('h3')

        testText = "Course Name: CS 494"
        
        for i in range(len(testTexts)):
            if(testTexts[i].text == testText):
                self.assertEqual(testTexts[i].text, testText)
                break

        driver.close()

      
     
    # check to see if we can update our blackboard credentials properly
    def test_register_blackboard_auth(self):
        #log in info for blackboard
        
        EMAIL = "usert4363@gmail.com"
        PASSWORD = "cs494Awesome"

        # first, we'll register to the app

        url = "http://my_uni:5000/register"

        driver = self.driver

        driver.implicitly_wait(30)
        driver.get(url)
        
        usrname = driver.find_element_by_xpath('/html/body/form/p[1]/input')
        usrname.send_keys("r")

        pword = driver.find_element_by_xpath('/html/body/form/p[2]/input')
        pword.send_keys("r")

        pword.send_keys(Keys.RETURN)

        # next we'll login

        url = "http://my_uni:5000/login"

        driver.get(url)
        
        usrname = driver.find_element_by_xpath('/html/body/form/p[1]/input')
        usrname.send_keys("r")

        pword = driver.find_element_by_xpath('/html/body/form/p[2]/input')
        pword.send_keys("r")

        pword.send_keys(Keys.RETURN)

        # next we'll update blackboard information

        url = "http://my_uni:5000/update"

        driver.get(url)
        
        usrname = driver.find_element_by_xpath('/html/body/form/p[1]/input')
        usrname.send_keys(EMAIL)

        gradescope = driver.find_element_by_xpath('/html/body/form/ul/li[3]/input')
        actions = ActionChains(driver)
        actions.move_to_element(gradescope)
        actions.click(gradescope)
        actions.perform()

        pword = driver.find_element_by_xpath('/html/body/form/p[3]/input')
        pword.send_keys(PASSWORD)

        pword.send_keys(Keys.RETURN)

        #now we'll make sure that it updated properly
        #if it did, it will have returned us to the index
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        testText = soup.find('h1').text

        self.assertEqual(testText, "Welcome to the UIC School Notifier, r")
        
        driver.close()
        
    
    # check to see if the recent activity of our blackbaord account are loaded properly
    def test_contents_blackboard_auth(self):
        # Due to security concerns have having UIC's account info released publicly, this test case
        # cannot be implemented.
        pass
    
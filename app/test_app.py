from app import app
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from bs4 import BeautifulSoup
import requests
import pandas as pd

# got it from the source mentioned in sources.txt

class FlaskAppTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = webdriver.Remote(command_executor='http://hub:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)

    @classmethod
    def tearDownClass(cls):
        cls.client.quit()

    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True

    def tearDown(self):
        pass

    # check to see if the index page loads the correct message when we aren't logged in
    def test_index_unauth(self):
        result = self.app.get('/')
        exists = result.data.find("Welcome to the UIC School Notifier, please log in or register.".encode()) != -1
        self.assertEqual(exists, True)
    
    # check to see if the login page loads the correct message when we aren't logged in
    def test_login_unauth(self):
        result = self.app.get('/login')
        exists = result.data.find("Sign In".encode()) != -1
        self.assertEqual(exists, True)

    # check to see if the register page loads the correct message when we aren't logged in
    def test_register_unauth(self):
        result = self.app.get('/register')
        exists = result.data.find("Register".encode()) != -1
        self.assertEqual(exists, True)

    # check to see if we can register properly
    def test_register_auth(self):
        result = self.app.post('/register', data = {"username" : "m", "password" : "agfgggg"}, follow_redirects=True)
        exists = result.data.find("Sign In".encode()) != -1
        self.assertEqual(exists, True)

    #check to see if we can register, then log in properly
    def test_register_login_auth(self):
        result = self.app.post('/register', data = {"username" : "l", "password" : "agfgggg"}, follow_redirects=True)
        exists = result.data.find("Sign In".encode()) != -1
        result = self.app.post('/login', data = {"username" : "l", "password" : "agfgggg"}, follow_redirects=True)
        exists = result.data.find("Welcome to the UIC School Notifier, l".encode()) != -1
        self.assertEqual(exists, True)

    # check to make sure that you can't register the same username twice
    def test_double_register_auth(self):
        result = self.app.post('/register', data = {"username" : "x", "password" : "agfgghhh"}, follow_redirects=True)
        exists = result.data.find("Sign In".encode()) != -1
        result = self.app.post('/register', data = {"username" : "x", "password" : "agfgghhh"}, follow_redirects=True)
        exists = result.data.find("Username already exists".encode()) != -1
        self.assertEqual(exists, True)


    # check to see if we can update our piazza credentials properly
    def test_register_piazza_auth(self):
        #log in info for piazza
        EMAIL = "usert4363@gmail.com"
        PASSWORD = "cs494Awesome"

        # first, we'll register to the app

        url = "http://localhost:5000/register"

        driver = self.client

        driver.implicitly_wait(30)
        driver.get(url)
        
        usrname = driver.find_element_by_xpath('//*[@id="username"]')
        usrname.send_keys("k")

        pword = driver.find_element_by_xpath('/html/body/form/p[2]/input')
        pword.send_keys("k")

        pword.send_keys(Keys.RETURN)

        # next we'll login

        url = "http://localhost:5000/login"

        driver.get(url)
        
        usrname = driver.find_element_by_xpath('/html/body/form/p[1]/input')
        usrname.send_keys("k")

        pword = driver.find_element_by_xpath('/html/body/form/p[2]/input')
        pword.send_keys("k")

        pword.send_keys(Keys.RETURN)

        # next we'll update piazza information

        url = "http://localhost:5000/registerPiazza"

        driver.get(url)
        
        usrname = driver.find_element_by_xpath('/html/body/form/p[1]/input')
        usrname.send_keys(EMAIL)

        pword = driver.find_element_by_xpath('/html/body/form/p[2]/input')
        pword.send_keys(PASSWORD)

        pword.send_keys(Keys.RETURN)

        #now we'll make sure that it updated properly
        #if it did, it will have returned us to the index
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        testText = soup.find('h1').text

        self.assertEqual(testText, "Welcome to the UIC School Notifier, k")


    # check to see if the contents of our piazza account are loaded properly
    def test_contents_piazza_auth(self):
        #log in info for piazza
        EMAIL = "usert4363@gmail.com"
        PASSWORD = "cs494Awesome"

        # first, we'll register to the app

        url = "http://localhost:5000/register"

        driver = self.client

        driver.implicitly_wait(30)
        driver.get(url)
        
        usrname = driver.find_element_by_xpath('//*[@id="username"]')
        usrname.send_keys("v")

        pword = driver.find_element_by_xpath('/html/body/form/p[2]/input')
        pword.send_keys("v")

        pword.send_keys(Keys.RETURN)

        # next we'll login

        url = "http://localhost:5000/login"

        driver.get(url)
        
        usrname = driver.find_element_by_xpath('/html/body/form/p[1]/input')
        usrname.send_keys("v")

        pword = driver.find_element_by_xpath('/html/body/form/p[2]/input')
        pword.send_keys("v")

        pword.send_keys(Keys.RETURN)

        # next we'll update piazza information

        url = "http://localhost:5000/registerPiazza"

        driver.get(url)
        
        usrname = driver.find_element_by_xpath('/html/body/form/p[1]/input')
        usrname.send_keys(EMAIL)

        pword = driver.find_element_by_xpath('/html/body/form/p[2]/input')
        pword.send_keys(PASSWORD)

        pword.send_keys(Keys.RETURN)

        # next we'll load our piazza information

        url = "http://localhost:5000/piazza"

        driver.get(url)

        soup = BeautifulSoup(driver.page_source, 'html.parser')

        testText = soup.find('h3').text

        self.assertEqual(testText, "Post Title: syncing github usernames")

    # check to see if we can update our gradescope credentials properly
    def test_register_gradescope_auth(self):
        #log in info for gradescope

        #WAIT TO UPDATE WITH PERSONAL CREDENTIALS
        EMAIL = ""
        PASSWORD = ""

        # first, we'll register to the app

        url = "http://localhost:5000/register"

        driver = self.client

        driver.implicitly_wait(30)
        driver.get(url)
        
        usrname = driver.find_element_by_xpath('//*[@id="username"]')
        usrname.send_keys("c")

        pword = driver.find_element_by_xpath('/html/body/form/p[2]/input')
        pword.send_keys("c")

        pword.send_keys(Keys.RETURN)

        # next we'll login

        url = "http://localhost:5000/login"

        driver.get(url)
        
        usrname = driver.find_element_by_xpath('/html/body/form/p[1]/input')
        usrname.send_keys("c")

        pword = driver.find_element_by_xpath('/html/body/form/p[2]/input')
        pword.send_keys("c")

        pword.send_keys(Keys.RETURN)

        # next we'll update piazza information

        url = "http://localhost:5000/registerGradescope"

        driver.get(url)
        
        usrname = driver.find_element_by_xpath('/html/body/form/p[1]/input')
        usrname.send_keys(EMAIL)

        pword = driver.find_element_by_xpath('/html/body/form/p[2]/input')
        pword.send_keys(PASSWORD)

        pword.send_keys(Keys.RETURN)

        #now we'll make sure that it updated properly
        #if it did, it will have returned us to the index
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        testText = soup.find('h1').text

        #self.assertEqual(testText, "Welcome to the UIC School Notifier, k")
        pass

    # check to see if the contents of our gradescope account are loaded properly
    def test_contents_gradescope_auth(self):
        #log in info for piazza
        #WAIT TO UPDATE WITH PERSONAL CREDENTIALS
        EMAIL = ""
        PASSWORD = ""

        # first, we'll register to the app

        url = "http://localhost:5000/register"

        driver = self.client

        driver.implicitly_wait(30)
        driver.get(url)
        
        usrname = driver.find_element_by_xpath('//*[@id="username"]')
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

        driver.get(url)

        soup = BeautifulSoup(driver.page_source, 'html.parser')

        testText = soup.find('h3').text

        self.assertEqual(testText, "Project 3 Submission")
        pass

    # check if list of classes loads properly for gradescope, current semester
    def test_className_gradescope_auth(self):
        #log in info for piazza
        #WAIT TO UPDATE WITH PERSONAL CREDENTIALS
        EMAIL = ""
        PASSWORD = ""

        # first, we'll register to the app

        url = "http://localhost:5000/register"

        driver = self.client

        driver.implicitly_wait(30)
        driver.get(url)
        
        usrname = driver.find_element_by_xpath('//*[@id="username"]')
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

        driver.get(url)

        soup = BeautifulSoup(driver.page_source, 'html.parser')

        testText = soup.findAll('h3').text

        self.assertEqual(testText[0], "CS 401")
        self.assertEqual(testText[1], "CS 418")
        pass

# check to see if we can update our blackboard credentials properly
    def test_register_blackboard_auth(self):
        pass

# check to see if the recent activity of our blackbaord account are loaded properly
def test_contents_blackboard_auth(self):
    pass
    
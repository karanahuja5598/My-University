#Sources: https://www.freecodecamp.org/news/better-web-scraping-in-python-with-selenium-beautiful-soup-and-pandas-d6390592e251/
#https://www.kenst.com/2015/03/including-the-chromedriver-location-in-macos-system-path/

# some of the pip packages we had to install:
#   pip3 install -U selenium
#   pip3 install chromedriver_installer
#   pip3 install BeautifulSoup4
#   pip3 install lxml

# function that gets us the information we need from piazza
def getGradescopeInfo(username, password):

    # we will need a web scraper to do this, since there is no API
    # the scraper we are using is selenium
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
    from bs4 import BeautifulSoup
    import requests
    import pandas as pd

    # set our username/email variable
    EMAIL = username
    # set our password variable
    PASSWORD = password

    # our gradescope url
    url = "http://www.gradescope.com/"

    # our web driver, this is like our 'browser'
    # we have a selenium hub docker image running
    # it has multiple 'chrome' nodes
    # this web driver will connect to one of those 'chrome' nodes
    driver = webdriver.Remote(command_executor='http://hub:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)

    # in case it takes a while, set our max waiting times
    driver.implicitly_wait(30)

    # fetch gradescope.com
    driver.get(url)

    # find the login button on the page
    loginButton = driver.find_element_by_xpath('/html/body/div/main/div[2]/div/header/nav/div[2]/span[3]/button')

    # click the login button
    actions = ActionChains(driver)
    actions.move_to_element(loginButton)
    actions.click(loginButton)
    actions.perform()

    # find the username field and fill it in with our email address
    usrname = driver.find_element_by_xpath('/html/body/div[1]/dialog/div/div[1]/form/div[1]/input')
    usrname.send_keys(EMAIL)

    # find the password field and fill it in with our password
    pword = driver.find_element_by_xpath('/html/body/div[1]/dialog/div/div[1]/form/div[2]/input')
    pword.send_keys(PASSWORD)

    # send enter, to basically attempt to login
    pword.send_keys(Keys.RETURN)

    # we will use beautiful soup to parse the webpage that we receive
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    # get our course lists
    allCourses = soup.find('div',{"class":"courseList"})

    # get our current semester course list
    # since it is find, and not findAll, it only gets the first occurence
    curSemCourses = allCourses.find('div')

    # these are the links to each course,
    # we will store them
    courseList = curSemCourses.findAll('a')
    courseLinks = []
    for i in courseList:
        courseLinks.append(url[:-1] + i.get('href'))

    # these are the names of each course,
    # we will store them
    courseNames = []
    for course in courseList:
        courseNames.append(course.find("h3").text)
    
    # the data of each course is stored as a table in gradescope
    # we will store each course info as a pandas dataframe, 
    # all in a list
    frames = []
    for x in courseLinks:
        # go to our course page
        driver.get(x)
        # use a new soup instance to parse
        soup1 = BeautifulSoup(driver.page_source, 'html.parser')
        # get our table with all our info
        tbl = soup1.find('table',{"id":"assignments-student-table"})
        # convert that table to a dataframe using pandas,
        # then append to our list of dataframes
        frames.append(pd.read_html(str(tbl))[0])

    # the array we will send containing all of the values
    # we found earlier
    gradescopeInfo = []

    # iterate through each course
    for i in range(len(courseNames)):
        # store all the course info in this dict
        courseDict = {}
        # set our course name
        courseDict["subject"] = courseNames[i]
        # store the content as an 'html' string
        courseDict["content"] = frames[i].to_html()
        # add to overall array
        gradescopeInfo.append(courseDict)

    # make sure to quit our driver
    driver.quit()

    # return our info
    return gradescopeInfo
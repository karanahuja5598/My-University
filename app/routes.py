# import the needed libraries
from quart import render_template, flash, redirect, url_for, session
from app import app
import app.forms as forms
from piazza import getPiazzaInfo
from gradescope import getGradescopeInfo
from bboard import getBlackboardInfo
import json
import asyncio
from threading import Thread

# set up pymongo
from flask_pymongo import PyMongo
mongo = PyMongo(app)

# this is the function we use to fetch and store any information we need
# from piazza, gradescope, or blackboard
# generally, we run this function on its own thread
def infoRunner(selector, mainUsername, username, password):

    # connect to our db
    userDB = mongo.cx["userDB"]
    userCollection = userDB["userCollection"]

    # get the needed info
    neededInfo = []
    if selector == "Piazza":
        neededInfo = getPiazzaInfo(username, password)
    elif selector == "Gradescope":
        neededInfo =  getGradescopeInfo(username, password)
    else:
        neededInfo = getBlackboardInfo(username, password)

    # convert the info into a json
    # this is so we can store it in mongo
    jsonInfo = json.dumps(neededInfo)

    # store the data in mongo
    userCollection.update(
        { "username" : mainUsername },
            { "$set" : 
                {
                    "data-"+selector : jsonInfo
                }
            }
    )
    return

# our home page route
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
async def index():

    # if the user is in the session, we do this:
    if("user" in session):

        # First, we connect to db
        userDB = mongo.cx["userDB"]
        userCollection = userDB["userCollection"]
        user = userCollection.find_one({ "username" : session["user"]["username"] })

        # now we build our userInfo object
        # which will be stored in sessions
        userInfo = {}
        userInfo["username"] = user["username"]
        userInfo["username-Piazza"] = user["username-Piazza"]
        userInfo["password-Piazza"] = user["password-Piazza"]
        userInfo["data-Piazza"] = user["data-Piazza"]
        userInfo["username-Gradescope"] = user["username-Gradescope"]
        userInfo["password-Gradescope"] = user["password-Gradescope"]
        userInfo["data-Gradescope"] = user["data-Gradescope"]
        userInfo["username-Blackboard"] = user["username-Blackboard"]
        userInfo["password-Blackboard"] = user["password-Blackboard"]
        userInfo["data-Blackboard"] = user["data-Blackboard"]

        # store in session
        session["user"] = userInfo

        # we find out if we can fetch the data
        canFetch = {"Piazza" : False, "Gradescope" : False, "Blackboard" : False}
        for selector in canFetch:
            if(("username-"+selector) in session["user"] and session["user"]["username-"+selector] != ""):
                canFetch[selector] = True

        # find out if there is data for each site stored in session
        hasData = {"Piazza" : False, "Gradescope" : False, "Blackboard" : False}

        # turn our json data in session back to its full data structure, and store it
        unraveledData = {"Piazza" : [], "Gradescope" : [], "Blackboard" : []}
        for selector in unraveledData:
            if(("data-"+selector) in session["user"] and session["user"]["data-"+selector] != ""):
                hasData[selector] = True
                unraveledData[selector] = json.loads(session["user"]["data-"+selector])

        # render our home page (logged in edition)
        return await render_template(
            'index.html', 
            title='Home', 
            loggedIn = True, 
            canFetch = canFetch,
            hasData = hasData, 
            user = session["user"], 
            unraveled = unraveledData)
    
    # render our home page (not logged in edition)s
    return await render_template('index.html', title='Home')

# our login route
@app.route('/login', methods=['GET', 'POST'])
async def login():

    # set up our login form
    form = forms.LoginForm()

    # if form was submitted and validated, then:
    if form.validate_on_submit():

        # connect to db
        userDB = mongo.cx["userDB"]
        userCollection = userDB["userCollection"]
        user = userCollection.find_one({ "username" : form.username.data })

        # if the user does not exist in db,
        # we can't login, flash a message,
        # go to homepage
        if user == None :
            await flash("Username does not exist")
            return redirect(url_for('login'))
        
        # if the password is wrong,
        # we can't login, flash a message,
        # go to homepage
        if form.password.data != user["password"] :
            await flash("Wrong password")
            return redirect(url_for('login'))

        # now we build our userInfo object
        # which will be stored in sessions
        userInfo = {}
        userInfo["username"] = user["username"]
        userInfo["username-Piazza"] = user["username-Piazza"]
        userInfo["password-Piazza"] = user["password-Piazza"]
        userInfo["data-Piazza"] = user["data-Piazza"]
        userInfo["username-Gradescope"] = user["username-Gradescope"]
        userInfo["password-Gradescope"] = user["password-Gradescope"]
        userInfo["data-Gradescope"] = user["data-Gradescope"]
        userInfo["username-Blackboard"] = user["username-Blackboard"]
        userInfo["password-Blackboard"] = user["password-Blackboard"]
        userInfo["data-Blackboard"] = user["data-Blackboard"]

        # store in session
        session["user"] = userInfo

        # go to index, but now we're logged in
        return redirect(url_for('index'))

    # render login page
    return await render_template('login.html', title='Sign In', form=form)

# our logout route
@app.route('/logout', methods=['GET', 'POST'])
async def logout():
    # it just pops the user from session
    if("user" in session):
        session.pop("user")
    # then we go back to index
    return redirect(url_for('index'))

# our register route
@app.route('/register', methods=['GET', 'POST'])
async def register():

    # set up our register form
    form = forms.RegisterForm()

    # if form was submitted and validated, then:
    if form.validate_on_submit():

        # connect to db
        userDB = mongo.cx["userDB"]
        userCollection = userDB["userCollection"]

        # if username was found, user already exists.
        # can't register, flash message,
        # redirect back here again
        if userCollection.find_one({ "username" : form.username.data }) != None :
            await flash('Username already exists')
            return redirect(url_for('register'))

        # otherwise, it's valid, we can register
        # store userinfo in db
        userCollection.insert_one(
            { "username" : form.username.data, "password" : form.password.data, 
                "username-Piazza" : "", "password-Piazza" : "", "data-Piazza" : "",
                "username-Gradescope" : "", "password-Gradescope" : "", "data-Gradescope" : "",
                "username-Blackboard" : "", "password-Blackboard" : "", "data-Blackboard" : "",})

        # flash that you are registered
        await flash("You are registered")
        # redirect to login page
        return redirect(url_for('login'))
    
    # render register page
    return await render_template('register.html', title='Register', form=form)

# our update login information route
@app.route('/update', methods=['GET', 'POST'])
async def update():

    # set up our update form
    form = forms.UpdateForm()

    # if form was submitted and validated, then:
    if form.validate_on_submit():

        # connect to db
        userDB = mongo.cx["userDB"]
        userCollection = userDB["userCollection"]
        selector = form.which.data

        # update data in db
        userCollection.update(
            { "username" : session["user"]["username"] },
                { "$set" : 
                    {
                        "username-"+selector : form.username.data,
                        "password-"+selector : form.password.data,
                        "data-"+selector : ""
                    }
                }
        )

        # now we build our userInfo object
        # which will be stored in sessions
        user = userCollection.find_one({ "username" : session["user"]["username"] })
        userInfo = {}
        userInfo["username"] = user["username"]
        userInfo["username-Piazza"] = user["username-Piazza"]
        userInfo["password-Piazza"] = user["password-Piazza"]
        userInfo["data-Piazza"] = user["data-Piazza"]
        userInfo["username-Gradescope"] = user["username-Gradescope"]
        userInfo["password-Gradescope"] = user["password-Gradescope"]
        userInfo["data-Gradescope"] = user["data-Gradescope"]
        userInfo["username-Blackboard"] = user["username-Blackboard"]
        userInfo["password-Blackboard"] = user["password-Blackboard"]
        userInfo["data-Blackboard"] = user["data-Blackboard"]

        # store in session
        session["user"] = userInfo
        
        # flash that the info was updated
        await flash("Updated info for " + selector)

        # redirect to index
        return redirect(url_for('index'))

    # render update page
    return await render_template('update.html', title='Update', form=form)




########
# The below three routes, are just fetchers of data
# they run our infoRunner() function
# this function runs on its own thread,
# then stores the information it gathers in mongo


@app.route('/fetchPiazza', methods=['GET', 'POST'])
async def fetchPiazza():
    selector = "Piazza"
    fetch = Thread(
        target=infoRunner,
        args = (
            selector, 
            session["user"]["username"], 
            session["user"]["username-"+selector], 
            session["user"]["password-"+selector]
        )
    )
    fetch.start()
    return redirect(url_for('index'))

@app.route('/fetchGradescope', methods=['GET', 'POST'])
async def fetchGradescope():
    selector = "Gradescope"
    fetch = Thread(
        target=infoRunner,
        args = (
            selector, 
            session["user"]["username"], 
            session["user"]["username-"+selector], 
            session["user"]["password-"+selector]
        )
    )
    fetch.start()
    return redirect(url_for('index'))

@app.route('/fetchBlackboard', methods=['GET', 'POST'])
async def fetchBlackboard():
    selector = "Blackboard"
    fetch = Thread(
        target=infoRunner,
        args = (
            selector, 
            session["user"]["username"], 
            session["user"]["username-"+selector], 
            session["user"]["password-"+selector]
        )
    )
    fetch.start()
    return redirect(url_for('index'))
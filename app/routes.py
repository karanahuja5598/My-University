#from flask import render_template, flash, redirect, url_for, session
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

#async def infoRunner(selector, mainUsername, username, password):
def infoRunner(selector, mainUsername, username, password):
    userDB = mongo.cx["userDB"]
    userCollection = userDB["userCollection"]
    neededInfo = []
    if selector == "Piazza":
        neededInfo = getPiazzaInfo(username, password)
    elif selector == "Gradescope":
        neededInfo =  getGradescopeInfo(username, password)
    else:
        neededInfo = getBlackboardInfo(username, password)
    jsonInfo = json.dumps(neededInfo)
    userCollection.update(
        { "username" : mainUsername },
            { "$set" : 
                {
                    "data-"+selector : jsonInfo
                }
            }
    )
    return



@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
async def index():
    #temp = getGradescopeInfo("blahblah@uic.edu","blahblah")
    #temp = getBlackboardInfo("blorg10@uic.edu", "blargaoe")
    if("user" in session):
        if("username-Piazza" in session["user"] and session["user"]["username-Piazza"] != ""):
            return await render_template('index.html', title='Home', loggedIn = True, piazza = True, user = session["user"])
        return await render_template('index.html', title='Home', loggedIn = True, user = session["user"])
    return await render_template('index.html', title='Home')

@app.route('/login', methods=['GET', 'POST'])
async def login():
    form = forms.LoginForm()
    if form.validate_on_submit():
        userDB = mongo.cx["userDB"]
        userCollection = userDB["userCollection"]
        user = userCollection.find_one({ "username" : form.username.data })
        if user == None :
            await flash("Username does not exist")
            return redirect(url_for('login'))
        if form.password.data != user["password"] :
            await flash("Wrong password")
            return redirect(url_for('login'))
        userInfo = {}
        userInfo["username"] = user["username"]
        userInfo["username-Piazza"] = user["username-Piazza"]
        userInfo["password-Piazza"] = user["password-Piazza"]
        userInfo["username-Gradescope"] = user["username-Gradescope"]
        userInfo["password-Gradescope"] = user["password-Gradescope"]
        userInfo["username-Blackboard"] = user["username-Blackboard"]
        userInfo["password-Blackboard"] = user["password-Blackboard"]
        session["user"] = userInfo
        return redirect(url_for('index'))
    return await render_template('login.html', title='Sign In', form=form)

@app.route('/register', methods=['GET', 'POST'])
async def register():
    form = forms.RegisterForm()
    if form.validate_on_submit():
        userDB = mongo.cx["userDB"]
        userCollection = userDB["userCollection"]
        if userCollection.find_one({ "username" : form.username.data }) != None :
            await flash('Username already exists')
            return redirect(url_for('register'))
        userCollection.insert_one(
            { "username" : form.username.data, "password" : form.password.data, 
                "username-Piazza" : "", "password-Piazza" : "",
                "username-Gradescope" : "", "password-Gradescope" : "",
                "username-Blackboard" : "", "password-Blackboard" : ""})
        await flash("You are registered")
        return redirect(url_for('login'))
    return await render_template('register.html', title='Register', form=form)

@app.route('/update', methods=['GET', 'POST'])
async def update():
    form = forms.UpdateForm()
    if form.validate_on_submit():
        userDB = mongo.cx["userDB"]
        userCollection = userDB["userCollection"]
        selector = form.which.data
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
        user = userCollection.find_one({ "username" : session["user"]["username"] })
        userInfo = {}
        userInfo["username"] = user["username"]
        userInfo["username-"+selector] = user["username-"+selector]
        userInfo["password-"+selector] = user["password-"+selector]
        session["user"] = userInfo
        await flash("Updated info for " + selector)
        #task = []
        #task = task.append(0)
        #task = asyncio.ensure_future(infoRunner(selector, userInfo["username"], userInfo["username-"+selector], userInfo["password-"+selector] ))
        thread = Thread(
            target=infoRunner,
            args = (selector, userInfo["username"], userInfo["username-"+selector], userInfo["password-"+selector]))
        thread.start()
        return redirect(url_for('index'))
    return await render_template('update.html', title='Update', form=form)



@app.route('/registerPiazza', methods=['GET', 'POST'])
async def registerPiazza():
    form = forms.LoginForm()
    if form.validate_on_submit():
        userDB = mongo.cx["userDB"]
        userCollection = userDB["userCollection"]
        userCollection.update(
            { "username" : session["user"]["username"] },
                { "$set" : 
                    {
                        "username-Piazza" : form.username.data,
                        "password-Piazza" : form.password.data
                    }
                }
        )
        user = userCollection.find_one({ "username" : session["user"]["username"] })
        userInfo = {}
        userInfo["username"] = user["username"]
        userInfo["username-Piazza"] = user["username-Piazza"]
        userInfo["password-Piazza"] = user["password-Piazza"]
        session["user"] = userInfo
        return redirect(url_for('index'))
    return await render_template('registerPiazza.html', title='Register', form=form)

@app.route('/piazza', methods=['GET', 'POST'])
async def piazza():
    #piazzaInfo = await getPiazzaInfo(session["user"]["username-Piazza"], session["user"]["password-Piazza"])
    #return await render_template('piazza.html', title='Register', posts = piazzaInfo)
    userDB = mongo.cx["userDB"]
    userCollection = userDB["userCollection"]
    user = userCollection.find_one({ "username" : session["user"]["username"] })
    neededInfo = user["data-Piazza"]
    if(len(neededInfo) != 0):
        neededInfo = json.loads(neededInfo)
        return await render_template('piazza.html', title='Register', posts = neededInfo)
    return redirect(url_for('index'))

@app.route('/registerGradescope', methods=['GET', 'POST'])
async def registerGradescope():
    form = forms.LoginForm()
    if form.validate_on_submit():
        userDB = mongo.cx["userDB"]
        userCollection = userDB["userCollection"]
        userCollection.update(
            { "username" : session["user"]["username"] },
                { "$set" : 
                    {
                        "username-Gradescope" : form.username.data,
                        "password-Gradescope" : form.password.data
                    }
                }
        )
        user = userCollection.find_one({ "username" : session["user"]["username"] })
        userInfo = {}
        userInfo["username"] = user["username"]
        userInfo["username-Gradescope"] = user["username-Gradescope"]
        userInfo["password-Gradescope"] = user["password-Gradescope"]
        session["user"] = userInfo
        return redirect(url_for('index'))
    return await render_template('registerGradescope.html', title='Register', form=form)

@app.route('/gradescope', methods=['GET', 'POST'])
async def gradescope():
    #gradescopeInfo = await getGradescopeInfo(session["user"]["username-Gradescope"], session["user"]["password-Gradescope"])
    #return await render_template('gradescope.html', title='Register', posts = gradescopeInfo)
    userDB = mongo.cx["userDB"]
    userCollection = userDB["userCollection"]
    user = userCollection.find_one({ "username" : session["user"]["username"] })
    neededInfo = user["data-Gradescope"]
    if(len(neededInfo) != 0):
        neededInfo = json.loads(neededInfo)
        return await render_template('gradescope.html', title='Register', posts = neededInfo)
    return redirect(url_for('index'))

@app.route('/registerBlackboard', methods=['GET', 'POST'])
async def registerBlackboard():
    form = forms.LoginForm()
    if form.validate_on_submit():
        userDB = mongo.cx["userDB"]
        userCollection = userDB["userCollection"]
        userCollection.update(
            { "username" : session["user"]["username"] },
                { "$set" : 
                    {
                        "username-Blackboard" : form.username.data,
                        "password-Blackboard" : form.password.data
                    }
                }
        )
        user = userCollection.find_one({ "username" : session["user"]["username"] })
        userInfo = {}
        userInfo["username"] = user["username"]
        userInfo["username-Blackboard"] = user["username-Blackboard"]
        userInfo["password-Blackboard"] = user["password-Blackboard"]
        session["user"] = userInfo
        return redirect(url_for('index'))
    return await render_template('registerBlackboard.html', title='Register', form=form)

@app.route('/blackboard', methods=['GET', 'POST'])
async def blackboard():
    blackboardInfo = await getBlackboardInfo(session["user"]["username-Blackboard"], session["user"]["password-Blackboard"])
    return await render_template('blackboard.html', title='Register', posts = blackboardInfo)
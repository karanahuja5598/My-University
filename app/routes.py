from flask import render_template, flash, redirect, url_for, session
from app import app
import app.forms as forms
from piazza import getPiazzaInfo
from gradescope import getGradescopeInfo

# set up pymongo
from flask_pymongo import PyMongo
mongo = PyMongo(app)

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    #temp = getGradescopeInfo("blahblah@uic.edu","blahblah")
    if("user" in session):
        if(session["user"]["username-Piazza"] != ""):
            return render_template('index.html', title='Home', loggedIn = True, piazza = True, user = session["user"])
        return render_template('index.html', title='Home', loggedIn = True, user = session["user"])
    return render_template('index.html', title='Home')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = forms.LoginForm()
    if form.validate_on_submit():
        userDB = mongo.cx["userDB"]
        userCollection = userDB["userCollection"]
        user = userCollection.find_one({ "username" : form.username.data })
        if user == None :
            flash("Username does not exist")
            return redirect(url_for('login'))
        if form.password.data != user["password"] :
            flash("Wrong password")
            return redirect(url_for('login'))
        userInfo = {}
        userInfo["username"] = user["username"]
        userInfo["username-Piazza"] = user["username-Piazza"]
        userInfo["password-Piazza"] = user["password-Piazza"]
        session["user"] = userInfo
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = forms.RegisterForm()
    if form.validate_on_submit():
        userDB = mongo.cx["userDB"]
        userCollection = userDB["userCollection"]
        if userCollection.find_one({ "username" : form.username.data }) != None :
            flash('Username already exists')
            return redirect(url_for('register'))
        userCollection.insert_one(
            { "username" : form.username.data, "password" : form.password.data, 
                "username-Piazza" : "", "password-Piazza" : "" })
        flash("You are registered")
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/registerPiazza', methods=['GET', 'POST'])
def registerPiazza():
    form = forms.PiazzaForm()
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
    return render_template('registerPiazza.html', title='Register', form=form)

@app.route('/piazza', methods=['GET', 'POST'])
def piazza():
    piazzaInfo = getPiazzaInfo(session["user"]["username-Piazza"], session["user"]["password-Piazza"])
    return render_template('piazza.html', title='Register', posts = piazzaInfo)
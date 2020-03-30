from flask import render_template, flash, redirect, url_for, session
from app import app
import app.forms as forms
from piazza import getPiazzaInfo

# set up pymongo
from flask_pymongo import PyMongo
mongo = PyMongo(app)

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = forms.PiazzaForm()
    if form.validate_on_submit():
        piazzaInfo = getPiazzaInfo(form.username.data, form.password.data)
        piazzaDB = mongo.cx["piazzaInfo"]
        piazzaCol = piazzaDB["theStuff"]
        piazzaCol.insert_one({"hi":"bye"})  
        return render_template('piazza.html', title = "Piazza Info", posts = piazzaInfo)
    return render_template('index.html', title='Home', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = forms.LoginForm()
    if form.validate_on_submit():
        userDB = mongo.cx["userDB"]
        userCollection = userDB["userCollection"]
        if userCollection.find_one({ "username" : form.username.data }) == None :
            flash("Username does not exist")
            return redirect(url_for('login'))
        
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
        userCollection.insert_one({ "username" : form.username.data, "password" : form.password.data })
        flash("You are registered")
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
from flask import render_template, flash, redirect, url_for
from app import app
import app.forms as forms
from piazza import getPiazzaInfo

# set up pymongo
from flask_pymongo import PyMongo
mongo = PyMongo(app)

from flask_login import LoginManager

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
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = forms.RegisterForm()
    return render_template('register.html', title='Register', form=form)
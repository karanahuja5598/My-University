from flask import Flask
from config import Config
from flask_pymongo import PyMongo

app = Flask(__name__)

# use config.py's Config class to set app config
app.config.from_object(Config)

# set up pymongo
mongo = PyMongo(app)

from app import routes
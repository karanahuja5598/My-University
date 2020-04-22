import quart.flask_patch
#from flask import Flask
from quart import Quart
from config import Config

#app = Flask(__name__)
app = Quart(__name__)

# use config.py's Config class to set app config
app.config.from_object(Config)

from app import routes
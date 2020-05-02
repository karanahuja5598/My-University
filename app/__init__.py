# to use flask addons with quart, we need the quart.flask_patch
import quart.flask_patch

# import quart
from quart import Quart
from config import Config

# initialize quart
app = Quart(__name__)

# use config.py's Config class to set app config
app.config.from_object(Config)

from app import routes

# NOTE:
#   We are using quart, instead of flask.
#   This is because flask is not very suited for asynchronous functionality.
#   We wanted to be able to fetch the data from the websites non synchronously.
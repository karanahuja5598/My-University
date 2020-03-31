import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'the-secret'

    # the mongo uri to connect from within the docker container
    MONGO_URI = 'mongodb://mongodb:27017/'

    WTF_CSRF_ENABLED = False
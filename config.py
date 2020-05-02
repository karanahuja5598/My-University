import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'the-secret'

    # the mongo uri to connect from within the docker container
    MONGO_URI = 'mongodb://mongodb:27017/'

    # this was causing issues with our scraper, so we disabled it
    WTF_CSRF_ENABLED = False
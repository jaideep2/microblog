import os

class Config(object):
    SECRET_KEY=os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    FLASK_DEBUG=os.environ.get('FLASK_DEBUG') or 1

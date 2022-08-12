#SECRET_KEY
from distutils.command.config import config
import os
from flask_sqlalchemy import SQLAlchemy
  

class DevelopmentConfig(config):
    DEBUG=True
    SECRET_KEY= '0f1bf7b724784b746e76e834'
    """ SQLAlchemy_DATABASE_URL= '/logindb.db' """

config={
    "development":DevelopmentConfig
}

os.urandom(12).hex()
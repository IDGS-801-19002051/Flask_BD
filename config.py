import os
from sqlalchemy import create_engine
import urllib

class Config(object):
  SECRET_KEY="clave nueva"
  SESSION_COOKIE_SECURE=False

class DevelopmentConfig(Config):
  DEBUG=True
  SQLALCHEMY_DATABASE_URI="mysql+pymysql://chekho:1234@127.0.0.1/bdidgs801"
  SQLALCHEMY_TRACK_MODIFICATIONS=False
  
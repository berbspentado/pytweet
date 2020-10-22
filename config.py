import os
from os.path import join,dirname
from dotenv import load_dotenv

dot_env = join(dirname(__file__),'.env')

class DevelopmentConfig():
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/oct_pytweet?charset=utf8'.format(**{
        'user':os.environ.get('MYSQL_USER','root'),
        'password':os.environ.get('MYSQL_PASSWORD',''),
        'host':os.environ.get('DB_HOST','localhost'),
    })

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

Config = DevelopmentConfig    
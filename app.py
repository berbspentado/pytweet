from flask import Flask
from .database import init_db
from .config import Config
import pytweet.models
import os

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.secret_key = os.urandom(24)
    init_db(app)
    return app

app = create_app()    
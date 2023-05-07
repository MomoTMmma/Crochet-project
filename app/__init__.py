from flask import Flask

from config import Config

from flask_login import LoginManager

app = Flask(__name__)

login = LoginManager()

app.config.from_object(Config)

from . import routes
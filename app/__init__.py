from flask import Flask
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

app = Flask(__name__)

app.config.from_pyfile('config.py')
app.secret_key = os.urandom(24)

mongo = PyMongo(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from app.home import home as home_blueprint
app.register_blueprint(home_blueprint)

from app.user import user as user_blueprint
app.register_blueprint(user_blueprint, url_prefix='/user')

from app.master import master as master_blueprint
app.register_blueprint(master_blueprint, url_prefix='/master')

login_manager.login_view = "home.login"

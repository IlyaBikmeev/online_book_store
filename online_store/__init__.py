import os

from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

load_dotenv()
app = Flask(__name__)
db = SQLAlchemy()
login_manager = LoginManager()
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'SQLALCHEMY_DATABASE_URI'
)

db.init_app(app)
login_manager.init_app(app)
from online_store.books_store.models import *
with app.app_context():
    db.create_all()

import online_store.books_store.views

from online_store.auth.views import auth
app.register_blueprint(auth)
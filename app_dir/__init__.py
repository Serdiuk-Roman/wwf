
# -*- coding: utf-8 -*-

from flask import Flask
from config import DevelopmentConfig
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)

app.config.from_object(DevelopmentConfig())

db = SQLAlchemy(app)
migrate = Migrate(app, db, render_as_batch=True)

login = LoginManager(app)
login.login_view = 'login'

bootstrap = Bootstrap(app)

moment = Moment(app)

toolbar = DebugToolbarExtension(app)


from app_dir import routes, models, errors

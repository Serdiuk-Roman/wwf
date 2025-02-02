
# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_debugtoolbar import DebugToolbarExtension
from config import DevelopmentConfig


db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'
login.login_message = 'Увійдіть, щоб отримати доступ до цієї сторінки.'
bootstrap = Bootstrap()
moment = Moment()
toolbar = DebugToolbarExtension()


def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)
    login.init_app(app)
    # mail.init_app(app)
    bootstrap.init_app(app)
    moment.init_app(app)
    toolbar.init_app(app)
    # babel.init_app(app)

    from app_dir.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from app_dir.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    from app_dir.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app_dir.new_elements import bp as new_elements_bp
    app.register_blueprint(new_elements_bp, url_prefix='/new_elements')

    from app_dir.order import bp as order_bp
    app.register_blueprint(order_bp)

    from app_dir.cw import bp as cw_bp
    app.register_blueprint(cw_bp, url_prefix='/cw')

    from app_dir.sketch import bp as sketch_bp
    app.register_blueprint(sketch_bp)

    # if not app.debug and not app.testing:
    #     if app.config['MAIL_SERVER']:
    #         auth = None
    #         if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
    #             auth = (app.config['MAIL_USERNAME'],
    #                     app.config['MAIL_PASSWORD'])
    #         secure = None
    #         if app.config['MAIL_USE_TLS']:
    #             secure = ()
    #         mail_handler = SMTPHandler(
    #             mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
    #             fromaddr='no-reply@' + app.config['MAIL_SERVER'],
    #             toaddrs=app.config['ADMINS'], subject='Microblog Failure',
    #             credentials=auth, secure=secure)
    #         mail_handler.setLevel(logging.ERROR)
    #         app.logger.addHandler(mail_handler)

    #     if not os.path.exists('logs'):
    #         os.mkdir('logs')
    #     file_handler = RotatingFileHandler('logs/microblog.log',
    #                                        maxBytes=10240, backupCount=10)
    #     file_handler.setFormatter(logging.Formatter(
    #         '%(asctime)s %(levelname)s: %(message)s '
    #         '[in %(pathname)s:%(lineno)d]'))
    #     file_handler.setLevel(logging.INFO)
    #     app.logger.addHandler(file_handler)

    #     app.logger.setLevel(logging.INFO)
    #     app.logger.info('Microblog startup')

    return app


# @babel.localeselector
# def get_locale():
#     return request.accept_languages.best_match(current_app.config['LANGUAGES'])


from app_dir import models

import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config():

    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True

    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(12).hex()


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False


class TestingConfig(Config):
    TESTING = True

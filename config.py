import os

# from sqlalchemy import event
# from sqlalchemy.engine import Engine
# from sqlite3 import Connection as SQLite3Connection

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')

    # @event.listens_for(Engine, "connect")
    # def _set_sqlite_pragma(dbapi_connection, connection_record):
    #     if isinstance(dbapi_connection, SQLite3Connection):
    #         cursor = dbapi_connection.cursor()
    #         cursor.execute("PRAGMA foreign_keys=ON;")
    #         cursor.close()

    SQLALCHEMY_TRACK_MODIFICATIONS = False

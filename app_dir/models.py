# from datetime import datetime

from app_dir import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Position(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # model_id = db.Column(db.String(32))
    # lutka_id = db.Column(db.String(32))

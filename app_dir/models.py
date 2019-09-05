from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from app_dir import db, login


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)


class BaseDecor(db.Model):
    __tablename__ = 'base_decors'
    id = db.Column(db.Integer, primary_key=True)
    indexname = db.Column(db.String(16), index=True, unique=True)
    decorname = db.Column(db.String(128), index=True, unique=True)
    door_models = db.relationship('DoorModel', backref='base_decor')

    def __repr__(self):
        return '<L:{}>'.format(self.decorname)


class SecondDecor(db.Model):
    __tablename__ = 'second_decors'
    id = db.Column(db.Integer, primary_key=True)
    indexname = db.Column(db.String(16), index=True, unique=True)
    decorname = db.Column(db.String(64), index=True, unique=True)
    door_models = db.relationship('DoorModel', backref='second_decor')

    def __repr__(self):
        return '<L:{}>'.format(self.decorname)


class LutkaVar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lutkaname = db.Column(db.String(64))
    thickness = db.Column(db.Integer)
    paz = db.Column(db.String(64))
    position_id = db.Column(
        db.Integer,
        db.ForeignKey('positions.id')
    )


class Block(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    height = db.Column(db.Integer)
    width = db.Column(db.Integer)
    thickness = db.Column(db.Integer)
    position_id = db.Column(
        db.Integer,
        db.ForeignKey('positions.id')
    )


class Zakaz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    positions = db.relationship('Position', backref='zakaz')

    def __repr__(self):
        return '<Zakaz_№{}>'.format(self.id)


class Position(db.Model):
    __tablename__ = 'positions'
    id = db.Column(db.Integer, primary_key=True)
    zakaz_id = db.Column(db.Integer, db.ForeignKey('zakaz.id'))
    room = db.Column(db.String(140))
    doormodel = db.relationship(
        'DoorModel',
        backref='position',
        uselist=False
    )
    lutkavar = db.relationship(
        'LutkaVar',
        backref='position',
        uselist=False
    )
    block_id = db.relationship(
        'Block',
        backref='position',
        uselist=False
    )


class DoorModel(db.Model):
    __tablename__ = 'door_models'
    id = db.Column(db.Integer, primary_key=True)
    modelname = db.Column(db.String(64), index=True, unique=True)
    position_id = db.Column(
        db.Integer,
        db.ForeignKey('positions.id')
    )
    basedecor_id = db.Column(
        db.Integer,
        db.ForeignKey('base_decors.id')
    )
    seconddecor_id = db.Column(
        db.Integer,
        db.ForeignKey('second_decors.id')
    )

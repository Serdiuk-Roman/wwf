from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from app_dir import db, login


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


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


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)


class Zakaz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    positions = db.relationship('Position', backref='dvery', lazy='dynamic')

    def __repr__(self):
        return '<Zakaz№{}>'.format(self.body)


# class CategoryDecor(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     category_name = db.Column(db.String(64), index=True, unique=True)

#     def __repr__(self):
#         return '<Вид:{}>'.format(self.category_name)


class Decor(db.Model):
    __tablename__ = 'decors'
    id = db.Column(db.Integer, primary_key=True)
    decorname = db.Column(db.String(64), index=True, unique=True)
    door_models = db.relationship('DoorModel', backref='decor')
    # category_id = db.Column(db.Integer, db.ForeignKey('categorydecor.id'))

    def __repr__(self):
        return '<L:{}>'.format(self.decorname)


class DoorModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    modelname = db.Column(db.String(64), index=True, unique=True)
    osnovapolotna_id = db.Column(db.Integer, db.ForeignKey('decors.id'))
    # decorpolotna_id = db.Column(db.Integer, db.ForeignKey('decor.id'))
    # decorcomplektacii_id = db.Column(db.Integer, db.ForeignKey('decor.id'))


class LutkaVar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lutkaname = db.Column(db.String(64), index=True)
    thickness = db.Column(db.Integer)
    paz = db.Column(db.String(64), index=True)


class Block(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    height = db.Column(db.Integer)
    width = db.Column(db.Integer)
    thickness = db.Column(db.Integer)


class Position(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    zakaz_id = db.Column(db.Integer, db.ForeignKey('zakaz.id'))
    room = db.Column(db.String(140))
    doormodel = db.relationship(
        'DoorModel',
        backref='door_model',
        lazy='dynamic'
    )
    lutkavar = db.relationship(
        'LutkaVar',
        backref='typ_lutky',
        lazy='dynamic'
    )
    block_id = db.relationship(
        'Block',
        backref='gabaryt',
        lazy='dynamic'
    )

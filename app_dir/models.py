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
    about_me = db.Column(db.String(140))
    # last_seen = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return 'User {}'.format(self.username)

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
        return 'Post {}'.format(self.body)


# class Zakaz(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     zakaz_number = db.Column(db.Integer)
#     timestamp = db.Column(db.DateTime, default=datetime.utcnow)
#     positions = db.relationship('Position', backref='zakaz')

#     def __repr__(self):
#         return 'Zakaz_№{}'.format(self.zakaz_number)


class Decor(db.Model):
    __tablename__ = 'decor'
    id = db.Column(db.Integer, primary_key=True)
    indexname = db.Column(db.String(16), index=True, unique=True)
    decorname = db.Column(db.String(128), index=True, unique=True)
    # 0 - laminate, 1 - cased_glass, 2 - glass_cleare, 3 - glass_plus
    decor_type = db.Column(db.String(4), index=True, unique=False)

    def __repr__(self):
        return 'Decor:{}'.format(self.decorname)


class DoorModel(db.Model):
    __tablename__ = 'door_models'
    id = db.Column(db.Integer, primary_key=True)
    positions = db.relationship(
        'Position',
        backref='doormodel'
    )
    modelname = db.Column(db.String(64), index=True, unique=True)

    laminate = db.Column(db.Boolean, default=False, nullable=False)
    cased_glass = db.Column(db.Boolean, default=False, nullable=False)
    glass_cleare = db.Column(db.Boolean, default=False, nullable=False)
    glass_plus = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self):
        return self.modelname


class FrameType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    frame_name = db.Column(db.String(16))
    expanders = db.relationship(
        'Position',
        backref='frame_type'
    )

    def __repr__(self):
        return self.frame_name


class Expander(db.Model):
    __tablename__ = 'expanders'
    id = db.Column(db.Integer, primary_key=True)
    expander_width = db.Column(db.Integer)
    expanders = db.relationship(
        'Position',
        backref='expander'
    )

    def __repr__(self):
        return '{} мм'.format(self.expander_width)


class Position(db.Model):
    __tablename__ = 'positions'
    id = db.Column(db.Integer, primary_key=True)
    room = db.Column(db.String(32))
    doormodel_id = db.Column(db.Integer, db.ForeignKey('door_models.id'))
    base_decor_id = db.Column(db.Integer, db.ForeignKey('decor.id'))
    second_decor_id = db.Column(db.Integer, db.ForeignKey('decor.id'))
    frame_id = db.Column(db.Integer, db.ForeignKey('frame_type.id'))
    doors_height = db.Column(db.Integer)
    doors_width = db.Column(db.Integer)
    expander_id = db.Column(db.Integer, db.ForeignKey('expanders.id'))

    # other_decor_id = db.Column(db.Integer, db.ForeignKey('decor.id'))
    # dl = db.relationship('Block', backref='position', uselist=False)

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
    orders = db.relationship('Order', backref='creator', lazy='dynamic')
    about_me = db.Column(db.String(140))
    # last_seen = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return self.username

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


class Decor(db.Model):
    __tablename__ = 'decor'
    id = db.Column(db.Integer, primary_key=True)
    indexname = db.Column(db.String(16), index=True, unique=True)
    decorname = db.Column(db.String(128), index=True, unique=True)
    # 0 - laminate, 1 - cased_glass, 2 - glass_cleare, 3 - glass_plus
    decor_type = db.Column(db.String(4), index=True, unique=False)

    def __repr__(self):
        return self.decorname


class DoorModel(db.Model):
    __tablename__ = 'door_models'
    id = db.Column(db.Integer, primary_key=True)
    modelname = db.Column(db.String(64), index=True, unique=True)

    laminate = db.Column(db.Boolean, default=False, nullable=False)
    cased_glass = db.Column(db.Boolean, default=False, nullable=False)
    glass_cleare = db.Column(db.Boolean, default=False, nullable=False)
    glass_plus = db.Column(db.Boolean, default=False, nullable=False)

    positions = db.relationship(
        'Position',
        backref='doormodel'
    )

    def __repr__(self):
        return self.modelname


class FrameType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    frame_name = db.Column(db.String(16))
    frames = db.relationship(
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


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    positions = db.relationship('Position', backref='order')
    order_number = db.Column(db.Integer, unique=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    positions = db.relationship('Position', backref='order')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    customer_manager = db.Column(db.String(64))
    customer_city = db.Column(db.String(64))

    def __repr__(self):
        return 'Заказ № {}'.format(self.order_number)


class Position(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))

    room = db.Column(db.String(32))
    doormodel_id = db.Column(db.Integer, db.ForeignKey('door_models.id'))

    base_decor_id = db.Column(db.Integer, db.ForeignKey('decor.id'))
    second_decor_id = db.Column(db.Integer, db.ForeignKey('decor.id'))

    base_decor = db.relationship('Decor', foreign_keys=[base_decor_id])
    second_decor = db.relationship('Decor', foreign_keys=[second_decor_id])

    frame_id = db.Column(db.Integer, db.ForeignKey('frame_type.id'))
    doors_height = db.Column(db.Integer)
    doors_width = db.Column(db.Integer)
    expander_id = db.Column(db.Integer, db.ForeignKey('expanders.id'))

    # other_decor_id = db.Column(db.Integer, db.ForeignKey('decor.id'))
    # dl = db.relationship('Block', backref='position', uselist=False)

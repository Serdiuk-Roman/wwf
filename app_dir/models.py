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


class OrderRemark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String())
    order_id = db.Column(
        db.Integer,
        db.ForeignKey('order.id'),
        index=True,
        unique=True
    )

    def __repr__(self):
        return self.body


class Decor(db.Model):
    __tablename__ = 'decor'
    id = db.Column(db.Integer, primary_key=True)
    indexname = db.Column(db.String(16))
    decorname = db.Column(db.String(128), index=True, unique=True)
    # 0 - laminate, 1 - cased_glass, 2 - glass_cleare, 3 - glass_plus
    decor_type = db.Column(db.String(4), index=True, unique=False)

    def __repr__(self):
        return self.indexname or self.decorname


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


class Casing(db.Model):
    __tablename__ = 'casings'
    id = db.Column(db.Integer, primary_key=True)
    casing_count = db.Column(db.String(16))
    casings = db.relationship(
        'Position',
        backref='casings_count'
    )

    def __repr__(self):
        return self.casing_count


class Expander(db.Model):
    __tablename__ = 'expanders'
    id = db.Column(db.Integer, primary_key=True)
    expander_width = db.Column(db.String(16))
    expanders = db.relationship(
        'Position',
        backref='expander'
    )

    def __repr__(self):
        return self.expander_width


class LocksPurpose(db.Model):
    """docstring for LocksPurpose"""
    __tablename__ = 'lock_purpose'
    id = db.Column(db.Integer, primary_key=True)
    purpose_name = db.Column(db.String(16))
    purposes = db.relationship(
        'Position',
        backref='lock_purpose'
    )

    def __repr__(self):
        return self.purpose_name


class LocksType(db.Model):
    """docstring for LocksType"""
    __tablename__ = 'lock_type'
    id = db.Column(db.Integer, primary_key=True)
    kind = db.Column(db.String(140))
    kinds = db.relationship(
        'Position',
        backref='lock_kind'
    )

    def __repr__(self):
        return self.kind


class LocksColor(db.Model):
    """docstring for LocksColor"""
    __tablename__ = 'lock_color'
    id = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.String(32))
    colors = db.relationship(
        'Position',
        backref='lock_color'
    )

    def __repr__(self):
        return self.color


class HingesSide(db.Model):
    """docstring for HingesSide"""
    __tablename__ = 'hinge_sides'
    id = db.Column(db.Integer, primary_key=True)
    side = db.Column(db.String(8))
    sides = db.relationship(
        'Position',
        backref='hinge_side'
    )

    def __repr__(self):
        return self.side


class HingesType(db.Model):
    """docstring for HingesType"""
    __tablename__ = 'hinge_types'
    id = db.Column(db.Integer, primary_key=True)
    kind = db.Column(db.String(140))
    kinds = db.relationship(
        'Position',
        backref='hinge_kind'
    )

    def __repr__(self):
        return self.kind


class HingesColor(db.Model):
    """docstring for HingesColor"""
    __tablename__ = 'hinge_colors'
    id = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.String(32))
    colors = db.relationship(
        'Position',
        backref='hinge_color'
    )

    def __repr__(self):
        return self.color


class DoorsSeal(db.Model):
    """docstring for DoorsSeal"""
    __tablename__ = 'door_seals'
    id = db.Column(db.Integer, primary_key=True)
    seal = db.Column(db.String(16))
    seals = db.relationship(
        'Position',
        backref='door_seal'
    )

    def __repr__(self):
        return self.seal


class AluminumButt(db.Model):
    """docstring for AluminumButt"""
    __tablename__ = 'aluminum_butts'
    id = db.Column(db.Integer, primary_key=True)
    butt_description = db.Column(db.String(64))
    butts = db.relationship(
        'Position',
        backref='alum_butt'
    )

    def __repr__(self):
        return self.butt_description


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    positions = db.relationship('Position', backref='order')
    order_number = db.Column(db.Integer, unique=True, index=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    positions = db.relationship('Position', backref='order')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    customer_manager = db.Column(db.String(64))
    customer_city = db.Column(db.String(64))

    ord_rem = db.relationship('OrderRemark', backref='remark', uselist=False)

    def __repr__(self):
        return 'Заказ № {}'.format(self.order_number)


class Position(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    serial_number = db.Column(db.Integer, index=True)

    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), index=True)

    room = db.Column(db.String(32))
    doormodel_id = db.Column(db.Integer, db.ForeignKey('door_models.id'))

    base_decor_id = db.Column(db.Integer, db.ForeignKey('decor.id'))
    second_decor_id = db.Column(db.Integer, db.ForeignKey('decor.id'))
    base_decor = db.relationship('Decor', foreign_keys=[base_decor_id])
    second_decor = db.relationship('Decor', foreign_keys=[second_decor_id])

    alum_butt_id = db.Column(db.Integer, db.ForeignKey('aluminum_butts.id'))

    frame_id = db.Column(db.Integer, db.ForeignKey('frame_type.id'))
    doors_height = db.Column(db.Integer)
    doors_width = db.Column(db.Integer)

    casing_id = db.Column(db.Integer, db.ForeignKey('casings.id'))
    expander_id = db.Column(db.Integer, db.ForeignKey('expanders.id'))

    lock_purpose_id = db.Column(db.Integer, db.ForeignKey('lock_purpose.id'))
    lock_kind_id = db.Column(db.Integer, db.ForeignKey('lock_type.id'))
    lock_color_id = db.Column(db.Integer, db.ForeignKey('lock_color.id'))

    hinge_side_id = db.Column(db.Integer, db.ForeignKey('hinge_sides.id'))
    hinge_kind_id = db.Column(db.Integer, db.ForeignKey('hinge_types.id'))
    hinge_color_id = db.Column(db.Integer, db.ForeignKey('hinge_colors.id'))

    doors_seal_id = db.Column(db.Integer, db.ForeignKey('door_seals.id'))

# -*- coding: utf-8 -*-


from app_dir import create_app, db
from app_dir.models import User, Post, Position, Decor, DoorModel, \
    Casing, Expander, FrameType, LocksPurpose, LocksType, LocksColor, \
    HingesSide, HingesType, HingesColor, DoorsSeal, AluminumButt


app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'User': User,
        'Post': Post,
        'Position': Position,
        'Decor': Decor,
        'DoorModel': DoorModel,
        'Casing': Casing,
        'Expander': Expander,
        'FrameType': FrameType,
        'LocksPurpose': LocksPurpose,
        'LocksType': LocksType,
        'LocksColor': LocksColor,
        'HingesSide': HingesSide,
        'HingesType': HingesType,
        'HingesColor': HingesColor,
        'DoorsSeal': DoorsSeal,
        'AluminumButt': AluminumButt

    }

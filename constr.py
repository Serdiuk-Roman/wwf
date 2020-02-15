# -*- coding: utf-8 -*-


from app_dir import app, db
from app_dir.models import User, Post, Decor, DoorModel, FrameType,  \
    Expander, Position


@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'User': User,
        'Post': Post,
        'Decor': Decor,
        'DoorModel': DoorModel,
        'FrameType': FrameType,
        'Expander': Expander,
        'Position': Position
    }

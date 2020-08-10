# -*- coding: utf-8 -*-

from flask import render_template
from flask_login import login_required

from app_dir import db

from app_dir.models import User

from app_dir.main import bp


@bp.route('/')
@bp.route('/index')
@login_required
def index():
    return render_template('index.html', title='Home')


@bp.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [

        {
            'author': user,
            'body': 'Test post #1'
        },
        {
            'author': user,
            'body': 'Test post #2'
        }
    ]
    return render_template('user.html', user=user, posts=posts)

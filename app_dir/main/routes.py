# -*- coding: utf-8 -*-

from flask import render_template, jsonify
from flask_login import login_required

# from app_dir import db

from app_dir.models import User, Decor, DoorModel

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


@bp.route('/ajax/change_base_decor/<int:doormodel_id>')
def base_decor(doormodel_id):

    doormodel = DoorModel.query.filter_by(id=doormodel_id).first()

    not_choice = {'id': 2, 'decorname': str(Decor.query.get_or_404(2))}

    base_decor_array = [not_choice, ]

    if doormodel.primer:
        base_decor_array.extend([
            {'id': d.id, 'decorname': d.decorname}
            for d in Decor.query.filter(Decor.primer)]
        )
    elif doormodel.paint:
        base_decor_array.extend([
            {'id': d.id, 'decorname': d.decorname}
            for d in Decor.query.filter(Decor.paint)]
        )
    elif doormodel.veneer:
        base_decor_array.extend([
            {'id': d.id, 'decorname': d.decorname}
            for d in Decor.query.filter(Decor.veneer)]
        )
    elif doormodel.laminate:
        base_decor_array.extend([
            {'id': d.id, 'decorname': d.decorname}
            for d in Decor.query.filter(Decor.laminate)]
        )
    else:
        empty_choice = {'id': 1, 'decorname': "Что то пошло не так"}
        base_decor_array = [empty_choice, ]
    return jsonify({'base_decor': base_decor_array})


@bp.route('/ajax/change_second_decor/<int:doormodel_id>')
def second_decor(doormodel_id):

    doormodel = DoorModel.query.filter_by(id=doormodel_id).first()

    empty_choice = {'id': 1, 'decorname': str(Decor.query.get_or_404(1))}
    not_choice = {'id': 2, 'decorname': str(Decor.query.get_or_404(2))}

    second_decor_array = [not_choice, ]

    if doormodel.cased_glass:
        second_decor_array.extend([
            {'id': d.id, 'decorname': d.decorname}
            for d in Decor.query.filter(Decor.cased_glass)]
        )
    elif doormodel.glass_cleare:
        second_decor_array.extend([
            {'id': d.id, 'decorname': d.decorname}
            for d in Decor.query.filter(Decor.glass_cleare)]
        )
    elif doormodel.glass_plus:
        second_decor_array.extend([
            {'id': d.id, 'decorname': d.decorname}
            for d in Decor.query.filter(Decor.glass_plus)]
        )
    else:
        second_decor_array = [empty_choice, ]
    return jsonify({'second_decor': second_decor_array})

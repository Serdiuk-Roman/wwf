# -*- coding: utf-8 -*-

from flask import render_template, jsonify
from flask_login import login_required

# from app_dir import db

from app_dir.models import User, Decor, DoorModel, CW_order, CW_vendor_code

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


@bp.route('/ajax/change_cw_vendor_code/<order_number>')
def cw_vendor_code(order_number):

    order = CW_order.query.filter_by(order_number=order_number).first()
    cw_vendor_code_list = CW_vendor_code.query.all()

    existing_cw_vendor_code_list = [
        vc.cw_vendor_code for vc in order.cw_positions
    ]

    clean_cw_vendor_code_list = [
        {'id': vendor_code.id, 'index': vendor_code.cw_vendor_code_index}
        for vendor_code in cw_vendor_code_list
        if vendor_code not in existing_cw_vendor_code_list
    ]

    return jsonify({'cw_vendor_code_list': clean_cw_vendor_code_list})


@bp.route('/ajax/cw_vendor_code_name/<id>')
def cw_vendor_code_name(id):

    vendor_code = CW_vendor_code.query.filter_by(id=id).first()

    return jsonify({'vendor_code_name': vendor_code.vendor_code_name})

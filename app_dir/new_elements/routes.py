# -*- coding: utf-8 -*-

from flask import render_template, flash, redirect, url_for
from flask_login import login_required

from app_dir import db

from app_dir.models import Decor, DoorModel

from app_dir.new_elements.forms import DecorForm, DoorModelForm

from app_dir.new_elements.the_first_data import load_data

from app_dir.new_elements import bp


@bp.route('/decor', methods=['get', 'post'])
@login_required
def decor():
    form = DecorForm()
    if form.validate_on_submit():
        decor = Decor(
            indexname=form.indexname.data,
            decorname=form.decorname.data,

            veneer=form.veneer.data,
            paint=form.paint.data,
            laminate=form.laminate.data,
            cased_glass=form.cased_glass.data,
            glass_cleare=form.glass_cleare.data,
            glass_plus=form.glass_plus.data
        )
        db.session.add(decor)
        db.session.commit()
        flash('Вы добавили новый декор.')
        return redirect(url_for('new_elements.decor'))
    decors = Decor.query.all()
    if not decors:
        flash('В базе еще нет декора')
    return render_template(
        'new_elements/decor.html',
        title='Декор',
        decors=decors,
        forms=form
    )


@bp.route('/door_model', methods=['get', 'post'])
@login_required
def door_model():
    form = DoorModelForm()
    if form.validate_on_submit():

        door_model = DoorModel(
            modelname=form.modelname.data,

            veneer=form.veneer.data,
            paint=form.paint.data,
            laminate=form.laminate.data,
            cased_glass=form.cased_glass.data,
            glass_cleare=form.glass_cleare.data,
            glass_plus=form.glass_plus.data
        )
        db.session.add(door_model)
        db.session.commit()
        flash('Вы добавили новую модель двери.')
        return redirect(url_for('new_elements.door_model'))
    door_models = DoorModel.query.all()
    if not door_models:
        flash('В базе еще пусто')
    return render_template(
        'new_elements/door_model.html',
        title='Модель',
        door_models=door_models,
        forms=form
    )


@bp.route('/first_data')
def first_data():

    gen_data = load_data()

    for i in gen_data:

        if not len(i['cls_name'].query.all()):

            for element in i['obj_list']:
                obj = i['cls_name'](**element)
                db.session.add(obj)
            db.session.commit()
            flash(i['msg'])

    return redirect(url_for('auth.register'))

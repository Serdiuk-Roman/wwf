# -*- coding: utf-8 -*-

from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

from app_dir import app, db
from app_dir.models import User, Decor, DoorModel, Position
from app_dir.forms import LoginForm, RegistrationForm, \
    DecorForm, DoorModelForm, PositionForm
from app_dir.utils import set_decor_type


@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html', title='Home')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html', user=user, posts=posts)


@app.route('/decor', methods=['get', 'post'])
@login_required
def decor():
    form = DecorForm()
    if form.validate_on_submit():
        decor = Decor(
            indexname=form.indexname.data,
            decorname=form.decorname.data,
            decor_type=set_decor_type(form.decor_type.data)

            # laminate=form.laminate.data or False,
            # cased_glass=form.laminate.data or False,
            # glass_cleare=form.laminate.data or False,
            # glass_plus=form.laminate.data or False

        )
        db.session.add(decor)
        db.session.commit()
        flash('Поздравляю, Вы добавили новый декор.')
        return redirect(url_for('decor'))
    decors = Decor.query.all()
    if not decors:
        flash('В базе еще нет декора')
    return render_template('decor.html', decors=decors, forms=form)


@app.route('/door_model', methods=['get', 'post'])
@login_required
def door_model():
    form = DoorModelForm()
    if form.validate_on_submit():

        door_model = DoorModel(
            modelname=form.modelname.data,
            laminate=form.laminate.data,
            cased_glass=form.cased_glass.data,
            glass_cleare=form.glass_cleare.data,
            glass_plus=form.glass_plus.data

        )
        db.session.add(door_model)
        db.session.commit()
        flash('Поздравляю, Вы добавили новую модель двери.')
        return redirect(url_for('door_model'))
    door_models = DoorModel.query.all()
    if not door_models:
        flash('В базе еще пусто')
    return render_template(
        'door_model.html',
        door_models=door_models,
        forms=form
    )


@app.route('/position', methods=['get', 'post'])
@login_required
def position():
    form = PositionForm()
    # print("---------------------------------------------")
    # print("")
    # print(form)
    # print(dir(form))
    # for i in dir(form):
    #     print(i, ' =:= ', request.form.get(i))
    if form.validate_on_submit():
        print("+++++++++++++++++++++++++++++++++++++++++++++")
        print(form.doormodel_id.data)

        position = Position(
            room=form.room.data,
            doormodel_id=form.doormodel_id.data,
            base_decor_id=form.base_decor_id.data,
            second_decor_id=form.second_decor_id.data,
            frame_id=form.frame_id.data,
            height_block=form.height_block.data,
            width_block=form.width_block.data,
            expander_id=form.expander_id.data,
            # other_decor_id=form.other_decor_id.data
        )
        db.session.add(position)
        db.session.commit()
        flash('Поздравляю, Вы добавили новую позицию.')
        return redirect(url_for('position'))
    if form.errors:
        print(form.errors)
    positions = Position.query.all()
    if not positions:
        flash('В базе еще пусто')
    return render_template(
        'position.html',
        positions=positions,
        forms=form
    )

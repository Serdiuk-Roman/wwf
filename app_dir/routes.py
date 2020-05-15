# -*- coding: utf-8 -*-

from datetime import datetime

from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

from app_dir import app, db

from app_dir.models import User, Decor, DoorModel, Position, Casing, \
    Expander, FrameType, Order, LocksPurpose, LocksType, LocksColor, \
    HingesSide

from app_dir.forms import LoginForm, RegistrationForm, DecorForm, \
    DoorModelForm, PositionForm, OrderForm

from app_dir.utils import set_decor_type, decor_list, door_model_list, \
    casings_list, expander_list, frame_type_list, locks_purpose_list, \
    locks_type_list, locks_color_list, hinge_sides_list


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
        )
        db.session.add(decor)
        db.session.commit()
        flash('Поздравляю, Вы добавили новый декор.')
        return redirect(url_for('decor'))
    decors = Decor.query.all()
    if not decors:
        flash('В базе еще нет декора')
    return render_template(
        'decor.html',
        title='Decor',
        decors=decors,
        forms=form
    )


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
        title='Model',
        door_models=door_models,
        forms=form
    )


@app.route('/first_data')
def first_data():

    if len(Decor.query.all()) is 0:

        for element in decor_list:
            decor = Decor(
                indexname=element['indexname'],
                decorname=element['decorname'],
                decor_type=element['decor_type']
            )
            db.session.add(decor)
        db.session.commit()
        flash('Поздравляю, Вы внесли первоначальный декор в базу!!!')

    if len(DoorModel.query.all()) is 0:

        for element in door_model_list:
            dm = DoorModel(
                modelname=element['modelname'],
                laminate=element['laminate'],
                cased_glass=element['cased_glass'],
                glass_cleare=element['glass_plus'],
                glass_plus=element['glass_cleare']
            )
            db.session.add(dm)
        db.session.commit()
        flash('Поздравляю, Вы внесли первоначальные модели в базу!!!')

    if len(Casing.query.all()) is 0:

        for element in casings_list:
            cas = Casing(
                casing_count=element['casing_count']
            )
            db.session.add(cas)
        db.session.commit()
        flash('Поздравляю, Вы внесли количество наличников в базу!!!')

    if len(Expander.query.all()) is 0:

        for element in expander_list:
            ex = Expander(
                expander_width=element['expander_width']
            )
            db.session.add(ex)
        db.session.commit()
        flash('Поздравляю, Вы внесли первоначальные доборы в базу!!!')

    if len(FrameType.query.all()) is 0:

        for element in frame_type_list:
            ft = FrameType(
                frame_name=element['frame_name']
            )
            db.session.add(ft)
        db.session.commit()
        flash('Поздравляю, Вы внесли типы луток в базу!!!')

    if len(LocksPurpose.query.all()) is 0:
        for element in locks_purpose_list:
            lp = LocksPurpose(
                purpose_name=element['purpose']
            )
            db.session.add(lp)
        db.session.commit()
        flash('Поздравляю, Вы внесли назначение замков!!!')

    if len(LocksType.query.all()) is 0:
        for element in locks_type_list:
            lt = LocksType(
                kind=element['kind']
            )
            db.session.add(lt)
        db.session.commit()
        flash('Поздравляю, Вы внесли тип замков!!!')

    if len(LocksColor.query.all()) is 0:
        for element in locks_color_list:
            lc = LocksColor(
                color=element['color']
            )
            db.session.add(lc)
        db.session.commit()
        flash('Поздравляю, Вы внесли цвет замков!!!')

    if len(HingesSide.query.all()) is 0:
        for element in hinge_sides_list:
            hs = HingesSide(
                side=element['side']
            )
            db.session.add(hs)
        db.session.commit()
        flash('Поздравляю, Вы внесли стороніь петель!!!')

    return redirect(url_for('register'))


@app.route('/orders', methods=['get'])
@login_required
def orders():
    orders = Order.query.all()
    return render_template(
        'orders.html',
        title='Ваши Заказы',
        orders=orders
    )


@app.route('/new_order', methods=['get', 'post'])
@login_required
def new_order():
    form = OrderForm()
    if form.validate_on_submit():
        order = Order(
            order_number=form.order_number.data,
            timestamp=datetime.utcnow(),
            creator=current_user,
            customer_manager=form.customer_manager.data,
            customer_city=form.customer_city.data
        )
        db.session.add(order)
        db.session.commit()
        flash('Поздравляю, Вы добавили новый заказ.')
        return redirect(url_for('order', order_number=order.order_number))
    return render_template(
        'new_order.html',
        title='Новый заказ',
        forms=form
    )


@app.route('/order/<int:order_number>', methods=['get', 'post'])
@login_required
def order(order_number):

    order = Order.query.filter_by(order_number=order_number).first_or_404()

    form = PositionForm()
    if form.validate_on_submit():
        position = Position(
            order_id=order.id,
            room=form.room.data,
            doormodel_id=form.doormodel_id.data,
            base_decor_id=form.base_decor_id.data,
            second_decor_id=form.second_decor_id.data,
            frame_id=form.frame_id.data,
            doors_height=form.doors_height.data,
            doors_width=form.doors_width.data,
            casing_id=form.casing_id.data,
            expander_id=form.expander_id.data,
            lock_purpose_id=form.lock_purpose_id.data,
            lock_type_id=form.lock_type_id.data,
            lock_color_id=form.lock_color_id.data
        )
        db.session.add(position)
        db.session.commit()
        flash('Поздравляю, Вы добавили новую позицию.')
        return redirect(url_for('order', order_number=order_number))
    if form.errors:
        print(form.errors)
    positions = Position.query.filter_by(order=order).all()
    if not positions:
        flash('Добавьте позиции')
    return render_template(
        'order.html',
        title='Заказ № {}'.format(order_number),
        order=order,
        positions=positions,
        forms=form
    )

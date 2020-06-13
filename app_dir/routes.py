# -*- coding: utf-8 -*-

from datetime import datetime

from flask import render_template, flash, redirect, url_for, request, jsonify
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

from app_dir import app, db

from app_dir.models import User, Decor, DoorModel, Position, Order, OrderRemark

from app_dir.forms import LoginForm, RegistrationForm, DecorForm, \
    DoorModelForm, PositionForm, OrderForm, OrderRemarkForm

from app_dir.the_first_data import load_data


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
        flash('Поздравляю, Вы теперь зареестрированый пользователь!')
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
            flash('Некоректное имя или пароль')
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
    return redirect(url_for('login'))


@app.route('/user/<username>')
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


@app.route('/decor', methods=['get', 'post'])
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
        return redirect(url_for('decor'))
    decors = Decor.query.all()
    if not decors:
        flash('В базе еще нет декора')
    return render_template(
        'decor.html',
        title='Декор',
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
        return redirect(url_for('door_model'))
    door_models = DoorModel.query.all()
    if not door_models:
        flash('В базе еще пусто')
    return render_template(
        'door_model.html',
        title='Модель',
        door_models=door_models,
        forms=form
    )


@app.route('/orders', methods=['get'])
@login_required
def orders():
    orders = Order.query.all()
    return render_template(
        'orders_list.html',
        title='Заказы',
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
        flash('Вы добавили новый заказ.')
        return redirect(url_for('order', order_number=order.order_number))
    return render_template(
        'order_form.html',
        title='Новый заказ',
        forms=form
    )


@app.route('/order/<int:order_number>', methods=['get', 'post'])
@login_required
def order(order_number):

    order = Order.query.filter_by(order_number=order_number).first()

    positions = Position.query.filter_by(order=order).all()
    remark = OrderRemark.query.filter_by(order_id=order.id).first()
    if not positions:
        flash('Добавьте позиции')
    return render_template(
        'order.html',
        title='Заказ № {}'.format(order_number),
        order=order,
        positions=positions,
        remark=remark
    )


@app.route('/order/<int:order_number>/add_position', methods=['get', 'post'])
@login_required
def add_order_position(order_number):

    order = Order.query.filter_by(order_number=order_number).first()

    form = PositionForm()
    if form.validate_on_submit():
        if len(order.positions):
            next_serial_number = max(
                [sn.serial_number for sn in order.positions]
            ) + 1
        else:
            next_serial_number = 1

        print()
        print(form.__dict__)
        print()

        position = Position(

            serial_number=next_serial_number,

            order_id=order.id,

            room=form.room.data,
            doormodel_id=form.doormodel_id.data,
            base_decor_id=form.base_decor_id.data,
            second_decor_id=form.second_decor_id.data,

            alum_butt_id=form.alum_butt_id.data,
            frame_id=form.frame_id.data,

            doors_height=form.doors_height.data,
            doors_width=form.doors_width.data,

            casing_id=form.casing_id.data,
            expander_id=form.expander_id.data,

            lock_purpose_id=form.lock_purpose_id.data,
            lock_kind_id=form.lock_kind_id.data,
            lock_color_id=form.lock_color_id.data,

            hinge_side_id=form.hinge_side_id.data,
            hinge_kind_id=form.hinge_kind_id.data,
            hinge_color_id=form.hinge_color_id.data,

            doors_seal_id=form.doors_seal_id.data
        )
        db.session.add(position)
        db.session.commit()
        flash('Вы добавили новую позицию.')
        return redirect(url_for('order', order_number=order_number))
    if form.errors:
        print()
        print('error:', form.errors)
        print()
    positions = Position.query.filter_by(order=order).all()
    if not positions:
        flash('Добавьте позиции')
    return render_template(
        'order_add_position.html',
        title='Заказ № {}'.format(order_number),
        order=order,
        positions=positions,
        forms=form
    )


@app.route('/order/<int:order_number>/remark_add', methods=['get', 'post'])
@login_required
def order_remark_add(order_number):

    order = Order.query.filter_by(order_number=order_number).first()
    positions = Position.query.filter_by(order=order).all()

    form = OrderRemarkForm()
    if form.validate_on_submit():

        rem = OrderRemark(
            body=form.body.data,
            order_id=order.id
        )
        db.session.add(rem)
        db.session.commit()
        flash('Вы добавили примечание')
        return redirect(url_for('order', order_number=order_number))
    if form.errors:
        print(form.errors)
    return render_template(
        'order_remark_add.html',
        title='Заказ № {}'.format(order_number),
        order=order,
        positions=positions,
        forms=form
    )


@app.route('/order/<int:order_number>/remark_edit', methods=['get', 'post'])
@login_required
def order_remark_edit(order_number):
    order = Order.query.filter_by(order_number=order_number).first_or_404()
    positions = Position.query.filter_by(order=order).all()
    remark = OrderRemark.query.filter_by(order_id=order.id).first()

    form = OrderRemarkForm(request.form, obj=remark)

    if request.method == 'POST' and form.validate_on_submit():

        remark.order_id = order.id

        form.populate_obj(remark)

        db.session.commit()
        flash('Вы изменили примечание')
        return redirect(url_for('order', order_number=order_number))
    if form.errors:
        print(form.errors)
    return render_template(
        'order_remark_edit.html',
        title='Заказ № {}'.format(order_number),
        order=order,
        positions=positions,
        forms=form
    )


@app.route('/order/<int:order_number>/remark_delete', methods=['post'])
@login_required
def order_remark_delete(order_number):
    order = Order.query.filter_by(order_number=order_number).first_or_404()
    remark = OrderRemark.query.filter_by(order_id=order.id).first_or_404()
    db.session.delete(remark)
    db.session.commit()
    return redirect(url_for('order', order_number=order_number))


@app.route('/ajax/change_base_decor/<int:doormodel_id>')
def base_decor(doormodel_id):

    doormodel = DoorModel.query.filter_by(id=doormodel_id).first()

    not_choice = {'id': 2, 'decorname': str(Decor.query.get_or_404(2))}

    base_decor_array = [not_choice, ]

    if doormodel.veneer:
        base_decor_array.extend([
            {'id': d.id, 'decorname': d.decorname}
            for d in Decor.query.filter(Decor.veneer)]
        )
    elif doormodel.paint:
        base_decor_array.extend([
            {'id': d.id, 'decorname': d.decorname}
            for d in Decor.query.filter(Decor.paint)]
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


@app.route('/ajax/change_second_decor/<int:doormodel_id>')
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


@app.route(
    '/order/<int:order_number>/<int:serial_number>',
    methods=['get', 'post'])
@login_required
def edit_order_position(order_number, serial_number):

    order = Order.query.filter_by(order_number=order_number).first_or_404()
    position = Position.query.\
        filter_by(order_id=order.id).\
        filter_by(serial_number=serial_number).\
        first_or_404()

    form = PositionForm(request.form, obj=position)

    if request.method == 'POST' and form.validate_on_submit():

        position.serial_number = serial_number

        position.order_id = order.id

        form.populate_obj(position)

        db.session.commit()
        flash('Вы изменили позицию № {}'.format(serial_number))
        return redirect(url_for('order', order_number=order_number))

    if form.errors:
        print(form.errors)
    return render_template(
        'position_edit.html',
        title='Заказ № {}'.format(order_number),
        order=order,
        position=position,
        forms=form
    )


@app.route(
    '/order/<int:order_number>/delete/<int:serial_number>',
    methods=['post'])
@login_required
def delete_order_position(order_number, serial_number):

    order = Order.query.filter_by(order_number=order_number).first_or_404()
    position = Position.query.\
        filter_by(order_id=order.id).\
        filter_by(serial_number=serial_number).\
        first_or_404()

    db.session.delete(position)

    last_positions = Position.query.\
        filter_by(order_id=order.id).\
        filter(Position.serial_number > serial_number).\
        all()

    if len(last_positions):
        for event in last_positions:
            event.serial_number -= 1

    db.session.commit()
    flash('Вы удалили позицию из заказа № {}'.format(order_number))
    return redirect(url_for('order', order_number=order_number))


@app.route('/scetch/<int:order_number>', methods=['post'])
@login_required
def gen_scetch(order_number):

    return "Hello {}".format(order_number)


@app.route('/first_data')
def first_data():

    gen_data = load_data()

    for i in gen_data:

        if not len(i['cls_name'].query.all()):

            for element in i['obj_list']:
                obj = i['cls_name'](**element)
                db.session.add(obj)
            db.session.commit()
            flash(i['msg'])

    return redirect(url_for('register'))

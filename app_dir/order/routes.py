# -*- coding: utf-8 -*-

from datetime import datetime

from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_required

from app_dir import db

from app_dir.models import Position, Order, OrderRemark

from app_dir.order.forms import PositionForm, OrderForm, OrderRemarkForm

from app_dir.order import bp


@bp.route('/orders', methods=['get'])
@login_required
def orders():
    orders = Order.query.all()
    return render_template(
        'order/orders_list.html',
        title='Заказы',
        orders=orders
    )


@bp.route('/new_order', methods=['get', 'post'])
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
        return redirect(
            url_for(
                'order.order',
                order_number=order.order_number
            )
        )
    return render_template(
        'order/order_form.html',
        title='Новый заказ',
        forms=form
    )


@bp.route('/order/<int:order_number>', methods=['get', 'post'])
@login_required
def order(order_number):

    order = Order.query.filter_by(order_number=order_number).first()

    positions = Position.query.filter_by(order=order).all()
    remark = OrderRemark.query.filter_by(order_id=order.id).first()
    if not positions:
        flash('Добавьте позиции')
    return render_template(
        'order/order.html',
        title='Заказ № {}'.format(order_number),
        order=order,
        positions=positions,
        remark=remark
    )


@bp.route('/order/<int:order_number>/add_position', methods=['get', 'post'])
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
        return redirect(url_for('order.order', order_number=order_number))
    if form.errors:
        print('error:', form.errors)
    positions = Position.query.filter_by(order=order).all()
    if not positions:
        flash('Добавьте позиции')
    return render_template(
        'order/order_add_position.html',
        title='Заказ № {}'.format(order_number),
        order=order,
        positions=positions,
        forms=form
    )


@bp.route('/order/<int:order_number>/remark_add', methods=['get', 'post'])
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
        return redirect(url_for('order.order', order_number=order_number))
    if form.errors:
        print(form.errors)
    return render_template(
        'order/order_remark_add.html',
        title='Заказ № {}'.format(order_number),
        order=order,
        positions=positions,
        forms=form
    )


@bp.route('/order/<int:order_number>/remark_edit', methods=['get', 'post'])
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
        return redirect(url_for('order.order', order_number=order_number))
    if form.errors:
        print(form.errors)
    return render_template(
        'order/order_remark_edit.html',
        title='Заказ № {}'.format(order_number),
        order=order,
        positions=positions,
        forms=form
    )


@bp.route('/order/<int:order_number>/remark_delete', methods=['post'])
@login_required
def order_remark_delete(order_number):
    order = Order.query.filter_by(order_number=order_number).first_or_404()
    remark = OrderRemark.query.filter_by(order_id=order.id).first_or_404()
    db.session.delete(remark)
    db.session.commit()
    return redirect(url_for('order.order', order_number=order_number))


@bp.route(
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
        return redirect(url_for('order.order', order_number=order_number))

    if form.errors:
        print(form.errors)
    return render_template(
        'order/position_edit.html',
        title='Заказ № {}'.format(order_number),
        order=order,
        position=position,
        forms=form
    )


@bp.route(
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
    return redirect(url_for('order.order', order_number=order_number))

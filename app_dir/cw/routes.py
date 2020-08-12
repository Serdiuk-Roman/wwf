# -*- coding: utf-8 -*-

from datetime import datetime

from flask import render_template, flash, redirect, url_for
from flask_login import login_required, current_user

from app_dir import db

from app_dir.models import CW_order, CW_position
from app_dir.cw.forms import CWOrderForm, CWPositionForm

from app_dir.cw import bp


@bp.route('/orders', methods=['get'])
@login_required
def orders():
    orders = CW_order.query.all()
    return render_template(
        'cw/orders_list.html',
        title='Заказы CW',
        orders=orders
    )


@bp.route('/new_order', methods=['get', 'post'])
@login_required
def new_order():
    form = CWOrderForm()
    if form.validate_on_submit():
        order = CW_order(
            order_number=form.order_number.data,
            customer_manager=form.customer_manager.data,
            customer_city=form.customer_city.data,
            timestamp=datetime.utcnow(),
            cw_creator=current_user
        )
        db.session.add(order)
        db.session.commit()
        flash('Вы добавили новый заказ.')
        return redirect(
            url_for(
                'cw.order',
                order_number=order.order_number
            )
        )
    return render_template(
        'cw/order_form.html',
        title='Новый заказ CW',
        forms=form
    )


@bp.route('/order/<order_number>', methods=['get', 'post'])
@login_required
def order(order_number):

    order = CW_order.query.filter_by(order_number=order_number).first()

    positions = CW_position.query.filter_by(cw_order=order).all()
    if not positions:
        flash('Добавьте позиции')
    return render_template(
        'cw/order.html',
        title='Заказ № {}'.format(order_number),
        order=order,
        positions=positions
    )


@bp.route('/order/<order_number>/add_position', methods=['get', 'post'])
@login_required
def add_order_position(order_number):

    order = CW_order.query.filter_by(order_number=order_number).first()

    form = CWPositionForm()
    if form.validate_on_submit():

        position = CW_position(

            cw_order_id=order.id,

            cw_vendor_code_id=form.cw_vendor_code_id.data,
            doors_quantity=form.doors_quantity.data,
        )
        db.session.add(position)
        db.session.commit()
        flash('Вы добавили новую позицию.')
        return redirect(url_for('cw.order', order_number=order_number))
    if form.errors:
        print('error:', form.errors)
    positions = CW_position.query.filter_by(cw_order=order).all()
    if not positions:
        flash('Добавьте позиции')
    return render_template(
        'cw/order_add_position.html',
        title='Заказ CW № {}'.format(order_number),
        order=order,
        positions=positions,
        forms=form
    )

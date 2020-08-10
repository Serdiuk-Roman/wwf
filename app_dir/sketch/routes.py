# -*- coding: utf-8 -*-

from flask import flash, redirect, url_for
from flask_login import login_required

from app_dir import db

from app_dir.models import Order

from app_dir.sketch import sketch_manager
from app_dir.sketch import bp


@bp.route('/sketch/<int:order_number>', methods=['post'])
@login_required
def gen_sketch(order_number):

    pg = sketch_manager.Pdf_Generator(order_number)
    pg.run()

    order = Order.query.filter_by(order_number=order_number).first()

    order.sketch_is_ready = True

    db.session.add(order)
    db.session.commit()
    flash('Добавлены єскизы')
    return redirect(url_for('main.order', order_number=order.order_number))

# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, NumberRange
from wtforms.widgets.html5 import NumberInput
# from wtforms.widgets import TextArea

from app_dir.models import CW_vendor_code, CW_position


class CWOrderForm(FlaskForm):
    order_number = StringField(
        'Заказ CW №',
        validators=[DataRequired()]
    )
    customer_manager = StringField('Дилер', validators=[DataRequired()])
    customer_city = StringField('Город', validators=[DataRequired()])

    submit = SubmitField('Добавить')


class CWPositionForm(FlaskForm):

    cw_vendor_code_id = SelectField(
        'Артикул',
        coerce=int,
        validators=[DataRequired()]
    )

    doors_quantity = IntegerField(
        'Количество полотен',
        widget=NumberInput(min='0', step='1'),
        validators=[NumberRange(
            min=0,
            message='Некоректное количество'
        )]
    )

    submit = SubmitField('Добавить')

    def __init__(self, *args, **kwargs):
        super(CWPositionForm, self).__init__(*args, **kwargs)

        self.cw_vendor_code_id.choices = \
            [(dm.id, dm.cw_vendor_code_index)
             for dm in CW_vendor_code.query.all()]


class CW_vendor_codeForm(FlaskForm):
    cw_vendor_code_index = IntegerField(
        'Артикул',
        widget=NumberInput(min='0', max='36', step='1'),
        validators=[NumberRange(
            min=0,
            max=36,
            message='Некоректный артикул'
        )]
    )
    article_name = StringField(
        'Наимен.',
        validators=[DataRequired()]
    )
    doors_height = IntegerField('Высота полотна')
    doors_width = IntegerField(
        'Ширина полотна',
        widget=NumberInput(min='600', max='900', step='100'),
        validators=[NumberRange(
            min=600,
            max=900,
            message='Некоректная ширина'
        )]
    )
    hinge_side = StringField(
        'Открывание',
        validators=[DataRequired()]
    )

    def __init__(self, *args, **kwargs):
        super(CW_position, self).__init__(*args, **kwargs)

        self.cw_vendor_code_id.choices = \
            [(dm.id, dm.cw_vendor_code_index)
             for dm in CW_vendor_code.query.all()]

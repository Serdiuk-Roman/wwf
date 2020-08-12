# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class DecorForm(FlaskForm):
    indexname = StringField('Индекс')
    decorname = StringField('Назва', validators=[DataRequired()])

    primer = BooleanField('Грунт')
    paint = BooleanField('Краска')
    veneer = BooleanField('Шпон')
    laminate = BooleanField('Плёнка')
    cased_glass = BooleanField('Накладное стекло')
    glass_cleare = BooleanField('Cleare')
    glass_plus = BooleanField('Plus')

    submit = SubmitField('Добавить')


class DoorModelForm(FlaskForm):
    modelname = StringField('Название', validators=[DataRequired()])

    primer = BooleanField('Грунт')
    paint = BooleanField('Краска')
    veneer = BooleanField('Шпон')
    laminate = BooleanField('Плёнка')
    cased_glass = BooleanField('Накладное стекло')
    glass_cleare = BooleanField('Cleare')
    glass_plus = BooleanField('Plus')

    submit = SubmitField('Добавить')

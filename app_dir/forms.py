# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class PozuciiaForm(FlaskForm):
    room = StringField('Комната', validators=[DataRequired()])
    model_ID = StringField('Модель', validators=[DataRequired()])
    lytka_ID = StringField('Тип лутки', validators=[DataRequired()])

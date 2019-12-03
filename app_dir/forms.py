# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, \
    SubmitField, RadioField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo

from app_dir.models import User, DoorModel, Decor


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')


class DecorForm(FlaskForm):
    indexname = StringField('Индекс', validators=[DataRequired()])
    decorname = StringField('Назва', validators=[DataRequired()])

    decor_type = RadioField(
        'Тип',
        choices=[
            ('0', 'Пленка'),
            ('1', 'Накладное'),
            ('2', 'Для Cleare'),
            ('3', 'Для Plus')
        ]
    )

    submit = SubmitField('Добавить')


class DoorModelForm(FlaskForm):
    modelname = StringField('Модель', validators=[DataRequired()])
    laminate = BooleanField('Плёнка', validators=[DataRequired()])
    cased_glass = BooleanField('Накладное стекло')
    glass_cleare = BooleanField('Cleare')
    glass_plus = BooleanField('Plus')

    submit = SubmitField('Добавить')


class PositionForm(FlaskForm):
    room = StringField('Комната', validators=[DataRequired()])
    doormodel_id = SelectField(
        'Модель', choices=[
            (dm.id, dm.modelname) for dm in DoorModel.query.all()
        ]
    )
    base_decor_id = SelectField(
        'Декор полотна', choices=[
            (d.id, d.decorname) for d in Decor.query.filter(
                Decor.decor_type == '1000'
            )
        ]
    )
    second_decor_id = SelectField(
        'Дополнительный декор', choices=[
            (d.id, d.decorname) for d in Decor.query.filter(
                Decor.decor_type == '0100',
                Decor.decor_type == '0010',
                Decor.decor_type == '0001'
            )
        ]
    )
    other_decor_id = SelectField(
        'Дополнительный декор', choices=[
            (d.id, d.decorname) for d in Decor.query.filter(
                Decor.decor_type == '1000',
                Decor.decor_type == '0010',
                Decor.decor_type == '0001'
            )
        ]
    )

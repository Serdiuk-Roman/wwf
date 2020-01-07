# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, \
    SubmitField, RadioField, SelectField, IntegerField, \
    DecimalField
from wtforms.validators import ValidationError, DataRequired, Email, \
    EqualTo, NumberRange
from wtforms.widgets.html5 import NumberInput

from app_dir.models import User, DoorModel, Decor, FrameType, Expander


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
    modelname = StringField('Название', validators=[DataRequired()])
    laminate = BooleanField('Плёнка', validators=[DataRequired()])
    cased_glass = BooleanField('Накладное стекло')
    glass_cleare = BooleanField('Cleare')
    glass_plus = BooleanField('Plus')

    submit = SubmitField('Добавить')


class PositionForm(FlaskForm):
    # pass
    room = StringField('Комната', validators=[DataRequired()])

    doormodel_id = SelectField(
        'Модель',
        validators=[DataRequired()],
        coerce=int,
        choices=[
            (dm.id, dm.modelname) for dm in DoorModel.query.all()
        ]
    )
    base_decor_id = SelectField(
        'Декор полотна',
        coerce=int,
        choices=[
            (d.id, d.decorname) for d in Decor.query.filter(
                Decor.decor_type == '1000'
            )
        ],
        validators=[DataRequired()]
    )
    second_decor_id = SelectField(
        'Дополнительный декор',
        coerce=int,
        choices=[
            (d.id, d.decorname) for d in Decor.query.filter(
                Decor.decor_type == '0100'
            )
        ]
    )
    frame_id = SelectField(
        'Тип лутки',
        coerce=int,
        choices=[
            (ft.id, ft.frame_name) for ft in FrameType.query.all()
        ]
    )
    height_block = IntegerField(
        'Высота блока',
        widget=NumberInput(min='1844', max='2294', step='10'),
        validators=[
            DataRequired(),
            NumberRange(
                min=1844,
                max=2294,
                message='Некоректная высота блока'
            )
        ]
    )
    width_block = IntegerField(
        'Ширина блока',
        widget=NumberInput(min='370', max='970', step='10'),
        validators=[NumberRange(
            min=370,
            max=970,
            message='Некоректная ширина блока'
        )]
    )
    expander_id = SelectField(
        'Добор',
        coerce=int,
        choices=[
            (er.id, er.expander_width) for er in Expander.query.all()
        ]
    )

    submit = SubmitField('Добавить')


class FrameTypeForm(FlaskForm):
    pass
#     frame_name = SelectField(
#         'Тип лутки', choices=[
#             (ft.id, ft.frame_name) for ft in Frame_type.query.all()
#         ]
#     )

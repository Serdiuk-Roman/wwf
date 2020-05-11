# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, \
    SubmitField, RadioField, SelectField, IntegerField
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

    room = StringField('Комната', validators=[DataRequired()])

    doormodel_id = SelectField(
        'Модель',
        coerce=int,
        validators=[DataRequired()]
    )
    base_decor_id = SelectField(
        'Декор полотна',
        coerce=int,
        validators=[DataRequired()]
    )
    second_decor_id = SelectField(
        'Дополнительный декор',
        coerce=int,
        validators=[DataRequired()]
    )
    frame_id = SelectField(
        'Тип лутки',
        coerce=int,
        validators=[DataRequired()]
    )
    doors_height = IntegerField(
        'Высота полотна',
        widget=NumberInput(min='1800', max='2240', step='10'),
        validators=[
            DataRequired(),
            NumberRange(
                min=1800,
                max=2240,
                message='Некоректная высота полотна'
            )
        ]
    )
    doors_width = IntegerField(
        'Ширина полотна',
        widget=NumberInput(min='550', max='900', step='10'),
        validators=[NumberRange(
            min=550,
            max=900,
            message='Некоректная ширина полотна'
        )]
    )
    expander_id = SelectField(
        'Добор',
        coerce=int
    )

    submit = SubmitField('Добавить')

    def __init__(self, *args, **kwargs):
        super(PositionForm, self).__init__(*args, **kwargs)

        self.doormodel_id.choices = \
            [(dm.id, dm.modelname) for dm in DoorModel.query.all()]

        self.base_decor_id.choices = \
            [(d.id, d.decorname) for d in Decor.query.filter(
                Decor.decor_type == '1000'
            )]
        without_decor = Decor.query.get_or_404(1)
        self.base_decor_id.choices.insert(
            0, (
                without_decor.id,
                without_decor.decorname
            )
        )

        self.second_decor_id.choices = \
            [(d.id, d.decorname) for d in Decor.query.filter(
                Decor.decor_type == '0100'
            )]
        self.second_decor_id.choices.extend(
            [(d.id, d.decorname) for d in Decor.query.filter(
                Decor.decor_type == '0010'
            )]
        )
        self.second_decor_id.choices.extend(
            [(d.id, d.decorname) for d in Decor.query.filter(
                Decor.decor_type == '0001'
            )]
        )
        empty = Decor.query.get_or_404(2)
        self.second_decor_id.choices.insert(
            0, (
                empty.id,
                empty.decorname
            )
        )

        self.frame_id.choices = \
            [(ft.id, ft.frame_name) for ft in FrameType.query.all()]
        # self.frame_id.choices.insert(0, (0, "Не выбрана"))

        self.expander_id.choices = \
            [(er.id, er.expander_width) for er in Expander.query.all()]
        # self.expander_id.choices.insert(0, (0, "Не выбран"))


class OrderForm(FlaskForm):
    order_number = IntegerField(
        'Заказ №',
        widget=NumberInput(min='17000', step='1'),
        validators=[DataRequired()]
    )
    customer_manager = StringField('Менеджер', validators=[DataRequired()])
    customer_city = StringField('Город', validators=[DataRequired()])

    submit = SubmitField('Добавить')

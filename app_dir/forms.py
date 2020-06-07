# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, \
    SubmitField, RadioField, SelectField, IntegerField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, \
    EqualTo, NumberRange
from wtforms.widgets.html5 import NumberInput
# from wtforms.widgets import TextArea

from app_dir.models import User, DoorModel, Decor, FrameType, Casing, \
    Expander, LocksPurpose, LocksType, LocksColor, HingesSide, HingesType, \
    HingesColor, DoorsSeal, AluminumButt


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Войти')


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
            raise ValidationError('Такое Имя существует, придумайте другое')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Используйте другой email, такой уже есть')


class DecorForm(FlaskForm):
    indexname = StringField('Индекс')
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


class OrderRemarkForm(FlaskForm):
    body = TextAreaField(
        'Примечание:'
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

    room = StringField('Помещение', validators=[DataRequired()])

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
    alum_butt_id = SelectField(
        'Алюминиевый торец',
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

    casing_id = SelectField(
        'Наличник',
        coerce=int
    )

    expander_id = SelectField(
        'Добор',
        coerce=int
    )

    lock_purpose_id = SelectField(
        'Назначение замка',
        coerce=int
    )

    lock_kind_id = SelectField(
        'Тип замка',
        coerce=int
    )

    lock_color_id = SelectField(
        'Цвет замка',
        coerce=int
    )

    hinge_side_id = SelectField(
        'Сторона петель',
        coerce=int
    )

    hinge_kind_id = SelectField(
        'Тип петель',
        coerce=int
    )

    hinge_color_id = SelectField(
        'Цвет петель',
        coerce=int
    )

    doors_seal_id = SelectField(
        'Уплотнитель',
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

        self.second_decor_id.choices = \
            [(d.id, d.decorname) for d in Decor.query.filter(
                Decor.decor_type == '0000'
            )]
        self.second_decor_id.choices.extend(
            [(d.id, d.decorname) for d in Decor.query.filter(
                Decor.decor_type == '0111'
            )]
        )
        # self.second_decor_id.choices.extend(
        #     [(d.id, d.decorname) for d in Decor.query.filter(
        #         Decor.decor_type == '0100'
        #     )]
        # )
        # self.second_decor_id.choices.extend(
        #     [(d.id, d.decorname) for d in Decor.query.filter(
        #         Decor.decor_type == '0010'
        #     )]
        # )
        # self.second_decor_id.choices.extend(
        #     [(d.id, d.decorname) for d in Decor.query.filter(
        #         Decor.decor_type == '0001'
        #     )]
        # )

        self.alum_butt_id.choices = \
            [(ab.id, ab.butt_description) for ab in AluminumButt.query.all()]

        self.frame_id.choices = \
            [(ft.id, ft.frame_name) for ft in FrameType.query.all()]

        self.casing_id.choices = \
            [(cas.id, cas.casing_count) for cas in Casing.query.all()]

        self.expander_id.choices = \
            [(er.id, er.expander_width) for er in Expander.query.all()]

        self.lock_purpose_id.choices = \
            [(lp.id, lp.purpose_name) for lp in LocksPurpose.query.all()]
        self.lock_kind_id.choices = \
            [(lt.id, lt.kind) for lt in LocksType.query.all()]
        self.lock_color_id.choices = \
            [(lc.id, lc.color) for lc in LocksColor.query.all()]

        self.hinge_side_id.choices = \
            [(hs.id, hs.side) for hs in HingesSide.query.all()]
        self.hinge_kind_id.choices = \
            [(ht.id, ht.kind) for ht in HingesType.query.all()]
        self.hinge_color_id.choices = \
            [(hc.id, hc.color) for hc in HingesColor.query.all()]

        self.doors_seal_id.choices = \
            [(ds.id, ds.seal) for ds in DoorsSeal.query.all()]


class OrderForm(FlaskForm):
    order_number = IntegerField(
        'Заказ №',
        widget=NumberInput(min='17000', step='1'),
        validators=[DataRequired()]
    )
    customer_manager = StringField('Дилер', validators=[DataRequired()])
    customer_city = StringField('Город', validators=[DataRequired()])

    submit = SubmitField('Добавить')

from app_dir.models import Decor, DoorModel, Casing, Expander, FrameType, \
    LocksPurpose, LocksType, LocksColor, HingesSide, HingesType, HingesColor, \
    DoorsSeal, AluminumButt

decor_list = dict(
    cls_name=Decor,
    msg='Внесен декор в базу',
    elm=[
        {
            'indexname': '',
            'decorname': 'Не выбран',
            'decor_type': '1000'
        },
        {
            'indexname': '',
            'decorname': 'Не выбрано',
            'decor_type': '0111'
        },
        {
            'indexname': '',
            'decorname': 'Отсутствует',
            'decor_type': '0000'
        },
        {
            'indexname': 'L1',
            'decorname': 'Дуб Сантана',
            'decor_type': '1000'
        },
        {
            'indexname': 'L3',
            'decorname': 'Дуб Ценамон',
            'decor_type': '1000'
        },
        {
            'indexname': 'L11',
            'decorname': 'Белый Матовый',
            'decor_type': '1000'
        },
        {
            'indexname': '',
            'decorname': 'Антрацит',
            'decor_type': '1000'
        },
        {
            'indexname': '4',
            'decorname': 'Зеркало Серебро',
            'decor_type': '0100'
        },
        {
            'indexname': '7',
            'decorname': 'Стекло прозрачное Сатин',
            'decor_type': '0010'
        },
        {
            'indexname': '1',
            'decorname': 'крашеное черное',
            'decor_type': '0100'
        }
    ]
)

door_model_list = dict(
    cls_name=DoorModel,
    msg='Внесены модели в базу!!!',
    elm=[
        {
            'modelname': 'Forte 10',
            'laminate': 1,
            'cased_glass': 0,
            'glass_cleare': 0,
            'glass_plus': 0,
        },
        {
            'modelname': 'Forte 12',
            'laminate': 1,
            'cased_glass': 1,
            'glass_cleare': 0,
            'glass_plus': 0,
        },
        {
            'modelname': 'Forte cleare 12',
            'laminate': 1,
            'cased_glass': 0,
            'glass_cleare': 1,
            'glass_plus': 0,
        }
    ]
)

casings_list = dict(
    cls_name=Casing,
    msg='Внесены наличники в базу!!!',
    elm=[
        {
            'casing_count': '2'
        },
        {
            'casing_count': '1'
        },
        {
            'casing_count': 'Нет'
        }
    ]
)

expander_list = dict(
    cls_name=Expander,
    msg='Внесены доборы в базу!!!',
    elm=[
        {
            'expander_width': 'Без паза'
        },
        {
            'expander_width': 'Паз под наличник'
        },
        {
            'expander_width': 'Нулевой добор'
        },
        {
            'expander_width': '50'
        },
        {
            'expander_width': '100'
        },
        {
            'expander_width': '150'
        },
        {
            'expander_width': '200'
        }
    ]
)

frame_type_list = dict(
    cls_name=FrameType,
    msg='Внесены типы луток в базу',
    elm=[
        {'frame_name': 'Форте'},
        {'frame_name': 'Стандарт'},
        {'frame_name': 'Француз'},
        {'frame_name': 'Англ'}
    ]
)

locks_purpose_list = dict(
    cls_name=LocksPurpose,
    msg='Внесены назначение замков',
    elm=[
        {'purpose_name': 'Нет'},
        {'purpose_name': 'BAD'},
        {'purpose_name': 'WC'},
        {'purpose_name': 'PZ'}
    ]
)

locks_type_list = dict(
    cls_name=LocksType,
    msg='Внесены типы замков',
    elm=[
        {'kind': 'Нет'},
        {'kind': 'AGB Evolution'},
        {'kind': 'AGB Polaris'},
        {'kind': 'Замок Заказчика'}
    ]
)

locks_color_list = dict(
    cls_name=LocksColor,
    msg='Внесены цвета замков',
    elm=[
        {'color': 'Нет'},
        {'color': 'Мат. Хром'},
        {'color': 'Никель'},
        {'color': 'Хром'},
        {'color': 'Старая бронза'},
        {'color': 'Бронза'},
        {'color': 'Черный'}
    ]
)

hinge_sides_list = dict(
    cls_name=HingesSide,
    msg='Внесены стороны петель',
    elm=[
        {'side': 'Нет'},
        {'side': 'Правая'},
        {'side': 'Левая'}
    ]
)

hinge_types_list = dict(
    cls_name=HingesType,
    msg='Внесены типы петель',
    elm=[
        {'kind': 'Нет'},
        {'kind': 'Anselmi 505 2 шт'},
        {'kind': 'Anselmi 505 3 шт'},
        {'kind': 'Anselmi 516 2 шт'},
        {'kind': 'Anselmi 516 3 шт'},
        {'kind': 'Флажковые 2 шт'},
        {'kind': 'Накладные 2 шт'}
    ]
)

hinge_colors_list = dict(
    cls_name=HingesColor,
    msg='Внесены цвета петель',
    elm=[
        {'color': 'Нет'},
        {'color': 'Мат. Хром'},
        {'color': 'Хром'},
        {'color': 'Бронза'}
    ]
)

door_seals_list = dict(
    cls_name=DoorsSeal,
    msg='Внесен уплотнитель',
    elm=[
        {'seal': 'Да'},
        {'seal': 'Нет'}
    ]
)

aluminum_butts_list = dict(
    cls_name=AluminumButt,
    msg='Внесены варианты алюминиевого торца',
    elm=[
        {'butt_description': 'Нет'},
        {'butt_description': 'По периметру'},
        {'butt_description': 'По 3-м'},
        {'butt_description': 'По бокам'},
        {'butt_description': 'Со стороны замка'},
        {'butt_description': 'Со стороны петель'}
    ]
)


def load_data():

    data_list = [
        decor_list,
        door_model_list,
        casings_list,
        expander_list,
        frame_type_list,
        locks_purpose_list,
        locks_type_list,
        locks_color_list,
        hinge_sides_list,
        hinge_types_list,
        hinge_colors_list,
        door_seals_list,
        aluminum_butts_list
    ]

    for point in data_list:
        yield dict(
            cls_name=point['cls_name'],
            obj_list=point['elm'],
            msg=point['msg']
        )

# if not len(Decor.query.all()):

#     for element in decor_list:
#         decor = Decor(
#             indexname=element['indexname'],
#             decorname=element['decorname'],
#             decor_type=element['decor_type']
#         )
#         db.session.add(decor)
#     db.session.commit()
#     flash('Поздравляю, Вы внесли первоначальный декор в базу!!!')

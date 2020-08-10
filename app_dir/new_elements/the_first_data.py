# -*- coding: utf-8 -*-

from app_dir.models import Decor, DoorModel, Casing, Expander, FrameType, \
    LocksPurpose, LocksType, LocksColor, HingesSide, HingesType, HingesColor, \
    DoorsSeal, AluminumButt

decor_list = dict(
    cls_name=Decor,
    msg='Внесен декор в базу',
    elm=[
        {
            'indexname': '',
            'decorname': 'Нет',
            'veneer': 0,
            'paint': 0,
            'laminate': 0,
            'cased_glass': 0,
            'glass_cleare': 0,
            'glass_plus': 0
        },
        {
            'indexname': '',
            'decorname': 'Не выбран',
            'veneer': 0,
            'paint': 0,
            'laminate': 0,
            'cased_glass': 0,
            'glass_cleare': 0,
            'glass_plus': 0
        },
        {
            'indexname': 'L1',
            'decorname': 'Дуб Сантана',
            'veneer': 0,
            'paint': 0,
            'laminate': 1,
            'cased_glass': 0,
            'glass_cleare': 0,
            'glass_plus': 0
        },
        {
            'indexname': 'Ш1',
            'decorname': 'Ясень',
            'veneer': 1,
            'paint': 0,
            'laminate': 0,
            'cased_glass': 0,
            'glass_cleare': 0,
            'glass_plus': 0
        },
        {
            'indexname': '',
            'decorname': 'Светлый грунт',
            'veneer': 0,
            'paint': 1,
            'laminate': 0,
            'cased_glass': 0,
            'glass_cleare': 0,
            'glass_plus': 0
        },
        {
            'indexname': '4',
            'decorname': 'Зеркало Серебро',
            'veneer': 0,
            'paint': 0,
            'laminate': 0,
            'cased_glass': 1,
            'glass_cleare': 0,
            'glass_plus': 0
        },
        {
            'indexname': '',
            'decorname': 'RAL 9003',
            'veneer': 0,
            'paint': 1,
            'laminate': 0,
            'cased_glass': 0,
            'glass_cleare': 0,
            'glass_plus': 0
        },
        {
            'indexname': '1',
            'decorname': 'Стекло крашеное черное',
            'veneer': 0,
            'paint': 1,
            'laminate': 0,
            'cased_glass': 0,
            'glass_cleare': 0,
            'glass_plus': 0
        },
        {
            'indexname': '',
            'decorname': 'Антрацит',
            'veneer': 0,
            'paint': 0,
            'laminate': 1,
            'cased_glass': 0,
            'glass_cleare': 0,
            'glass_plus': 0
        },
        {
            'indexname': '7',
            'decorname': 'Стекло t=6 прозрачное Сатин',
            'veneer': 0,
            'paint': 0,
            'laminate': 0,
            'cased_glass': 0,
            'glass_cleare': 1,
            'glass_plus': 0
        },
        {
            'indexname': '7',
            'decorname': 'Стекло t=8 прозрачное Сатин',
            'veneer': 0,
            'paint': 0,
            'laminate': 0,
            'cased_glass': 0,
            'glass_cleare': 0,
            'glass_plus': 1
        },
        {
            'indexname': '7',
            'decorname': 'Стекло t=10 прозрачное Сатин',
            'veneer': 0,
            'paint': 0,
            'laminate': 0,
            'cased_glass': 0,
            'glass_cleare': 0,
            'glass_plus': 1
        },

    ]
)

door_model_list = dict(
    cls_name=DoorModel,
    msg='Внесены модели в базу!!!',
    elm=[
        {
            'modelname': 'Evolushion 03 primer',
            'veneer': 0,
            'paint': 1,
            'laminate': 0,
            'cased_glass': 0,
            'glass_cleare': 0,
            'glass_plus': 0,
        },
        {
            'modelname': 'Forte 10',
            'veneer': 0,
            'paint': 0,
            'laminate': 1,
            'cased_glass': 0,
            'glass_cleare': 0,
            'glass_plus': 0,
        },
        {
            'modelname': 'Forte 12',
            'veneer': 0,
            'paint': 0,
            'laminate': 1,
            'cased_glass': 1,
            'glass_cleare': 0,
            'glass_plus': 0,
        },
        {
            'modelname': 'Forte cleare 12',
            'veneer': 0,
            'paint': 0,
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
            'expander_width': 'Нет'
        },
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
        {'frame_name': 'Форте ШпКр'},
        {'frame_name': 'Форте Пл'},
        {'frame_name': 'Стандарт'},
        {'frame_name': 'Француз'},
        {'frame_name': 'Англ'},
        {'frame_name': 'Алюм. Наруж'},
        {'frame_name': 'Алюм. Внутр'}
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

# -*- coding: utf-8 -*-

from app_dir.models import Decor, DoorModel, Casing, Expander, FrameType, \
    LocksPurpose, LocksType, LocksColor, HingesSide, HingesType, HingesColor, \
    DoorsSeal, AluminumButt, CW_vendor_code

decor_list = dict(
    cls_name=Decor,
    msg='Внесен декор в базу',
    elm=[
        {
            'indexname': '',
            'decorname': 'Нет',
            'primer': 0,
            'paint': 0,
            'veneer': 0,
            'laminate': 0,
            'cased_glass': 0,
            'glass_cleare': 0,
            'glass_plus': 0
        },
        {
            'indexname': '',
            'decorname': 'Не выбран',
            'primer': 0,
            'paint': 0,
            'veneer': 0,
            'laminate': 0,
            'cased_glass': 0,
            'glass_cleare': 0,
            'glass_plus': 0
        },
        {
            'indexname': 'L1',
            'decorname': 'Дуб Сантана',
            'primer': 0,
            'paint': 0,
            'veneer': 0,
            'laminate': 1,
            'cased_glass': 0,
            'glass_cleare': 0,
            'glass_plus': 0
        },
        {
            'indexname': 'Ш1',
            'decorname': 'Ясень',
            'primer': 0,
            'paint': 0,
            'veneer': 1,
            'laminate': 0,
            'cased_glass': 0,
            'glass_cleare': 0,
            'glass_plus': 0
        },
        {
            'indexname': '',
            'decorname': 'Светлый грунт',
            'primer': 1,
            'paint': 0,
            'veneer': 0,
            'laminate': 0,
            'cased_glass': 0,
            'glass_cleare': 0,
            'glass_plus': 0
        },
        {
            'indexname': '4',
            'decorname': 'Зеркало Серебро',
            'primer': 0,
            'paint': 0,
            'veneer': 0,
            'laminate': 0,
            'cased_glass': 1,
            'glass_cleare': 0,
            'glass_plus': 0
        },
        {
            'indexname': '',
            'decorname': 'RAL 9003',
            'primer': 0,
            'paint': 1,
            'veneer': 0,
            'laminate': 0,
            'cased_glass': 0,
            'glass_cleare': 0,
            'glass_plus': 0
        },
        {
            'indexname': '1',
            'decorname': 'Стекло крашеное черное',
            'primer': 0,
            'paint': 1,
            'veneer': 0,
            'laminate': 0,
            'cased_glass': 0,
            'glass_cleare': 0,
            'glass_plus': 0
        },
        {
            'indexname': '',
            'decorname': 'Антрацит',
            'primer': 0,
            'paint': 0,
            'veneer': 0,
            'laminate': 1,
            'cased_glass': 0,
            'glass_cleare': 0,
            'glass_plus': 0
        },
        {
            'indexname': '7',
            'decorname': 'Стекло t=6 прозрачное Сатин',
            'primer': 0,
            'paint': 0,
            'veneer': 0,
            'laminate': 0,
            'cased_glass': 0,
            'glass_cleare': 1,
            'glass_plus': 0
        },
        {
            'indexname': '7',
            'decorname': 'Стекло t=8 прозрачное Сатин',
            'primer': 0,
            'paint': 0,
            'veneer': 0,
            'laminate': 0,
            'cased_glass': 0,
            'glass_cleare': 0,
            'glass_plus': 1
        },
        {
            'indexname': '7',
            'decorname': 'Стекло t=10 прозрачное Сатин',
            'primer': 0,
            'paint': 0,
            'veneer': 0,
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
            'primer': 1,
            'paint': 0,
            'veneer': 0,
            'laminate': 0,
            'cased_glass': 0,
            'glass_cleare': 0,
            'glass_plus': 0,
        },
        {
            'modelname': 'Forte 10',
            'primer': 0,
            'paint': 0,
            'veneer': 0,
            'laminate': 1,
            'cased_glass': 0,
            'glass_cleare': 0,
            'glass_plus': 0,
        },
        {
            'modelname': 'Forte 12',
            'primer': 0,
            'paint': 0,
            'veneer': 0,
            'laminate': 1,
            'cased_glass': 1,
            'glass_cleare': 0,
            'glass_plus': 0,
        },
        {
            'modelname': 'Forte cleare 12',
            'primer': 0,
            'paint': 0,
            'veneer': 0,
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

vendor_code_list = dict(
    cls_name=CW_vendor_code,
    msg='Внесен артикул складской програміь',
    elm=[
        {
            'cw_vendor_code_index': '1',
            'vendor_code_name': '№1_нар_2000_600_прав.',
            'doors_height': 2000,
            'doors_width': 600,
            'hinge_side': 'Правое'
        },
        {
            'cw_vendor_code_index': '2',
            'vendor_code_name': '№2_нар_2000_600_лев.',
            'doors_height': 2000,
            'doors_width': 600,
            'hinge_side': 'Левое'
        },
        {
            'cw_vendor_code_index': '3',
            'vendor_code_name': '№3_нар_2000_700_прав.',
            'doors_height': 2000,
            'doors_width': 700,
            'hinge_side': 'Правое'
        },
        {
            'cw_vendor_code_index': '4',
            'vendor_code_name': '№4_нар_2000_700_лев.',
            'doors_height': 2000,
            'doors_width': 700,
            'hinge_side': 'Левое'
        },
        {
            'cw_vendor_code_index': '5',
            'vendor_code_name': '№5_нар_2000_800_прав.',
            'doors_height': 2000,
            'doors_width': 800,
            'hinge_side': 'Правое'
        },
        {
            'cw_vendor_code_index': '6',
            'vendor_code_name': '№6_нар_2000_800_лев.',
            'doors_height': 2000,
            'doors_width': 800,
            'hinge_side': 'Левое'
        },
        {
            'cw_vendor_code_index': '7',
            'vendor_code_name': '№7_нар_2000_900_прав.',
            'doors_height': 2000,
            'doors_width': 900,
            'hinge_side': 'Правое'
        },
        {
            'cw_vendor_code_index': '8',
            'vendor_code_name': '№8_нар_2000_900_лев.',
            'doors_height': 2000,
            'doors_width': 900,
            'hinge_side': 'Левое'
        }
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
        aluminum_butts_list,
        vendor_code_list
    ]

    for point in data_list:
        yield dict(
            cls_name=point['cls_name'],
            obj_list=point['elm'],
            msg=point['msg']
        )

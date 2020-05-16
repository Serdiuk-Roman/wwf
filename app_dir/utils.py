def set_decor_type(index):
    varlist = ['0', '0', '0', '0']
    varlist[int(index)] = '1'
    return ''.join(varlist)


decor_list = [
    {'indexname': '0', 'decorname': 'Не выбран', 'decor_type': '0000'},
    {'indexname': 'G', 'decorname': 'Стекло/Зеркало', 'decor_type': '0111'},
    {'indexname': 'empty', 'decorname': 'Отсутствует', 'decor_type': '0000'},
    {'indexname': 'L11', 'decorname': 'Белый Матовый', 'decor_type': '1000'},
    {'indexname': 'L1', 'decorname': 'Дуб Сантана', 'decor_type': '1000'},
    {'indexname': '4', 'decorname': 'Зеркало Серебро', 'decor_type': '0100'},
    {
        'indexname': '7',
        'decorname': 'Стекло прозрачное Сатин',
        'decor_type': '0010'
    },
    {'indexname': '1', 'decorname': 'крашеное черное', 'decor_type': '0100'},
    {'indexname': 'L3', 'decorname': 'Дуб Ценамон', 'decor_type': '1000'}
]

door_model_list = [
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

casings_list = [
    {
        'casing_count': None
    },
    {
        'casing_count': 1
    },
    {
        'casing_count': 2
    }
]

expander_list = [
    {
        'expander_width': None
    },
    {
        'expander_width': 0
    },
    {
        'expander_width': 50
    },
    {
        'expander_width': 100
    },
    {
        'expander_width': 150
    },
    {
        'expander_width': 200
    }
]

frame_type_list = [
    {'frame_name': "Форте"},
    {'frame_name': "Француз"}
]

locks_purpose_list = [
    {'purpose': None},
    {'purpose': "BAD"},
    {'purpose': "WC"},
    {'purpose': "PZ"}
]

locks_type_list = [
    {'kind': None},
    {'kind': "AGB Evolution"},
    {'kind': "AGB Polaris"},
    {'kind': "Замок Заказчика"}
]

locks_color_list = [
    {'color': None},
    {'color': "Мат. Хром"},
    {'color': "Никель"},
    {'color': "Хром"},
    {'color': "Старая бронза"},
    {'color': "Бронза"},
    {'color': "Черніьй"}
]

hinge_sides_list = [
    {'side': None},
    {'side': "Правая"},
    {'side': "Левая"}
]

hinge_types_list = [
    {'kind': None},
    {'kind': 'Anselmi 505 2 шт'},
    {'kind': 'Anselmi 505 3 шт'},
    {'kind': 'Anselmi 516 2 шт'},
    {'kind': 'Anselmi 516 3 шт'},
    {'kind': 'Флажковые 2 шт'},
    {'kind': 'Накладные 2 шт'}
]

hinge_colors_list = [
    {'color': None},
    {'color': "Мат. Хром"},
    {'color': "Хром"},
    {'color': "Бронза"}
]

door_seals_list = [
    {'seal': True},
    {'seal': None}
]

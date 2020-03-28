def set_decor_type(index):
    varlist = ['0', '0', '0', '0']
    varlist[int(index)] = '1'
    return ''.join(varlist)


decor_list = [
    {'indexname': '0', 'decorname': 'Не определен', 'decor_type': '0000'},
    {'indexname': 'L3', 'decorname': 'Дуб Ценамон', 'decor_type': '1000'},
    {'indexname': 'L11', 'decorname': 'Белый Матовый', 'decor_type': '1000'},
    {'indexname': 'L1', 'decorname': 'Дуб Сантана', 'decor_type': '1000'},
    {'indexname': '4', 'decorname': 'Зеркало Серебро', 'decor_type': '0100'},
    {'indexname': '7', 'decorname': 'Стекло прозрачное Сатин', 'decor_type': '0010'},
    {'indexname': '1', 'decorname': 'крашеное черное', 'decor_type': '0100'}
]

door_model_list = [
    {
        'modelname': 'Пустая',
        'laminate': 0,
        'cased_glass': 0,
        'glass_cleare': 0,
        'glass_plus': 0,
    },
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

expander_list = [
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
    {
        'frame_name': "Форте"
    },
    {
        'frame_name': "Француз"
    }
]

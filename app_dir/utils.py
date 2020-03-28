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
    {sss},
]


id,modelname,laminate,cased_glass,glass_cleare,glass_plus
1,Forte 12,1,1,0,0
2,Forte 10,1,0,0,0
3,Forte cleare 12,1,0,1,0
4,Forte plus 12,1,0,0,1

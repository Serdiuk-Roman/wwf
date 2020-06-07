def set_decor_type(index):
    varlist = ['0', '0', '0', '0']
    varlist[int(index)] = '1'
    return ''.join(varlist)

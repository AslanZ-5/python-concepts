def inx_item(item,inx):
    return item[inx]


try:
    inx_item([1,2,3],4)
except IndexError as a:
    print(f'got error -- {a}')

finally:
    print('The end')
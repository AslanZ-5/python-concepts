# def inx_item(item,inx):
#     return item[inx]
#
#
# try:
#     inx_item([1,2,3],4)
# except IndexError as a:
#     print(f'got error -- {a}')
#
# finally:
#     print('The end')

b = [1]
try:
    print(b[32])
except ZeroDivisionError:
    print('dddi')
else:
    print('else')

finally:
    print('get error')
print('print it ')
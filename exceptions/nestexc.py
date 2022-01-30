def action2():
    print(1 + [])


def action1():
    try:
        action2()
    except TypeError:  # Most recent matching try
        print('Inner Try')


try:
    action1()
except TypeError:
    print('outer try')

try:
    try:
        action2()
    except TypeError:
        print('---inner')
except TypeError:
    print('--- outer')


# # Try/Finally
# try:
#     try:
#         raise IndexError
#     finally:
#         print('span')
# finally:
#     print('smap')


def raise1():
    raise IndexError


def noraise():
    return


def raise2():
    raise SyntaxError

# for func in (raise1,noraise,raise2):
#     print('<%s>' % func.__name__)
#     try:
#         try:
#             func()
#         except IndexError:
#             print('caught IndexError')
#     finally:
#         print('Finnally run ')
#     print('.........')

class ExitLoop(Exception):pass
try:
    while True:
        while True:
            for i in range(10):
                if i > 3 :
                    raise ExitLoop
                print(f'loop3: {i}')
            print('loop2')
        print('loop1')
except ExitLoop:
    print('continuing')
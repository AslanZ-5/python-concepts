def test_decorator(func):
    print('befor')
    func()
    print('after')


@test_decorator
def do_stuff():
    print('doing stuff')


def makeBold(func):
    def inner():
        print('<b>')
        func()
        print('</b>')

    return inner


@makeBold
def NamePrint():
    print('Bryan Cairns')


NamePrint()


# Decorator with parameters

def numcheck(func):
    def checkInt(d):
        if isinstance(d, int):
            if d == 0:
                print('Can\'t divide by zero')
                return False
            return True
        print(f'{d} in not a number')
        return False

    def inner(x, y):
        if not checkInt(x) or not checkInt(y):
            return
        return func(x, y)

    return inner


@numcheck
def divide(a, b):
    print(a / b)


# Decorator with unknown number fo params
# We want a decorator that can pass params and handle anything
# we also want to chain them together
# *args, **kwargs to the rescue

def outline(func):
    def inner(*args, **kwargs):
        print('~' * 20)
        func(*args, **kwargs)
        print('~' * 20)

    return inner


def list_items(func):
    def inner(*args, **kwargs):
        func(*args, **kwargs)
        # print(f'args = {args}')
        # print(f'kwargs = {kwargs}')
        for i in args:
            print(f'args = {i}')
        for k, v in kwargs.items():
            print(f'key={k} value={v}')

    return inner


@outline
@list_items
def display(msg):
    print(msg)


display(msg=433)

a = {'as': 342, 'dd': 34}
print(a.items())
print(a.values())
print(a.keys())


def multipliers():
    return [lambda x, i=i: i * x for i in range(4)]


print([m(2) for m in multipliers()])
print(multipliers())

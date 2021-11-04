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
        if isinstance(d,int):
            if d == 0:
                print('Can\'t divide by zero')
                return False
            return True
        print(f'{d} in not a number')
        return False


    def inner(x, y):
        if not checkInt(x) or not checkInt(y):
            return
        return func(x,y)
    return inner

@numcheck
def divide(a, b):
    print(a / b)





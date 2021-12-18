class Spam:
    def doit(self, message):
        print(message)


if __name__ == '__main__':
    object1 = Spam()
    t = Spam.doit
    t(object1, 'heeeew')


class Eggs:
    def m1(self, n):
        print(n)

    def m2(self):
        x = self.m1
        x(42)


if __name__ == '__main__':
    d = Eggs()
    d.m2()


class Selfless:
    def __init__(self, data):
        self.data = data

    def selfless(arg1, arg2):
        return arg1 + arg2

    def normal(self, arg1, arg2):
        return self.data + arg1 + arg2


if __name__ == '__main__':
    X = Selfless(2)
    print(X.normal(3, 4))
    print(Selfless.normal(X, 4, 5))
    print(Selfless.selfless(4, 5))


class Number:
    def __init__(self, base):
        self.base = base

    def double(self):
        return self.base * 2

    def triple(self):
        return self.base * 3


if __name__ == "__main__":
    print('++++++++++++++')
    x = Number(2)
    y = Number(3)
    r = Number(4)
    t = Number(5)
    acts = [x.double, y.double, r.double, t.double]
    for i in acts:
        print(i())

    bound = x.double
    print(bound.__self__)
    print(bound.__func__)


def square(arg):
    return arg ** 2


class Sum:
    def __init__(self, val):
        self.val = val

    def __call__(self, arg):
        return self.val + arg


class Product:
    def __init__(self, val):
        self.val = val

    def method(self, arg):
        return self.val * arg


if __name__ == "__main__":
    sobject = Sum(2)
    print(sobject(4))
    pobject = Product(3)
    actions = [square, sobject, pobject.method]
    for i in actions:
        print(i(5))
class Wrapper:
    def __init__(self, object):
        self.wrapper = object

    def __getattr__(self, item):
        print(f'Trace {item}')
        return getattr(self.wrapper, item)


class A:
    def __str__(self):
        return 'classA'


class D:
    def __str__(self):
        return 'classD'


class B(A, D):
    def __str__(self):
        return D.__str__(self)


a = B()
print(a)

X = D()

X.a = 2
D.a = 12
print(X.a)
J = D()
print(J.a)

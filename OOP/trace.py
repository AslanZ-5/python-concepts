class Wrapper:
    def __init__(self,object):
        self.wrapper = object

    def __getattr__(self, item):
        print(f'Trace {item}')
        return getattr(self.wrapper, item)

class D:
    a = 1

X = D()

X.a = 2
D.a = 12
print(X.a)
J = D()
print(J.a)
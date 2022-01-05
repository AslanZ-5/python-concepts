class C:
    __slots__ = ['a', 'b']


class Slotful:
    __slots__ = ['a', 'b', '__dict__']

    def __init__(self, data):
        self.c = data


# Slots in sub but not super
class T:
    pass


class D(T):
    __slots__ = ['a']


X = D()
X.a = 1
X.b = 2
# print(X.__dict__)
# print(D.__dict__.keys())

# slot in super but not sub
class Y:
    __slots__ = ['a']
class R(Y):
    pass

I  = R()
I.a = 1
I.b = 2
print(I.__dict__)
print(Y.__dict__.keys())
# only lowerst slot accssible
class W: __slots__ = ['a']
class U(W): __slots__ = ['a']

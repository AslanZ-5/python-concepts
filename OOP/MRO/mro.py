class X:pass
class A:
    attr = 1


class B(X):
    pass


class C(A):
    attr = 2


class D(B, C):
    attr = C.attr


x = D()

print(B.__bases__)
print(A.__bases__)
print(C.__bases__)
print(D.__bases__)
print(D.mro())
print(D.__mro__)
class A:
    num = 10
class B(A):
    pass
class C(A):
    num = 1
class D(B, C):
    pass


class Y:
    pass
class Z:
    pass
class X:
    pass
class B(Y,Z):
    pass
class A(X,Y):
    pass
class M(B,A,Z):
    pass

print(M.mro())

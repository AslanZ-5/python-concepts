X = 1
def nester():
    X = 2
    print(X ,'nester enclosing scope')
    class C:
        X = 4 #Class local hides nester's
        print(X, 'class local scope')
        def method(self):
            print(X, 'method local')
            print(self.X)
        def method2(self):
            X = 3
            print(X)

    i = C()
    i.method()
    i.method2()

class Super:
    def hello(self):
        self.data1 = 'spam'
class Sub(Super):
    def hola(self):
        self.data2 = 'eggs'

# x = Sub()
# x.hello()
# x.hola()
# print(x.__dict__)
# print(x.__dict__.values())
# print(Sub.__dict__.keys())
# print(Super.__dict__.keys())
# print(x.__class__)
# print(Sub.__bases__)
# print(Super.__bases__)


def classtree(cls,indent):
    print('_' *indent + cls.__name__)
    for supercls in cls.__bases__:
        classtree(supercls,indent+3)

def instancetree(inst):
    print(f'Tree of {inst}')
    classtree(inst.__class__,3)

def selftest():
    class A: pass
    class B(A): pass

    class C(A): pass

    class D(B, C): pass

    class E: pass

    class F(D, E): pass
    instancetree(B())
    instancetree(F())
if __name__ == '__main__':
    selftest()







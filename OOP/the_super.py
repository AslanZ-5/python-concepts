class A:
    def __init__(self):
        print('init A')
    def act(self):
        print('A')


class B:
    def __init__(self):
        super().__init__()
        print('init b')
    def act(self):
        print('B')


class C(A,B):
    def __init__(self):
        super().__init__()
    def act(self):
        super().act()



a = A()
b = B()
c = C()
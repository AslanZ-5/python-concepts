class A:
    def act(self):
        print('A')


class B:
    def act(self):
        print('B')


class C(A, B):
    def act(self):
        B.act(self)

x = C()
x.act()
class C1:
    def meth1(self):
        self.__X = 88

    def meth2(self):
        print(self.__X)


class C2:
    def metha(self):
        self.__X = 99

    def methb(self):
        print(self.__X)


class C3(C1, C2):
    pass


class Super:
    def method(self):
        print('this is method func')

class Tool:
    def __method(self):
        print(f'using only inside the {self.__class__.__name__} class')

    def other(self):
        print(f'methd -- {self.__method()}')

class Sub1(Tool,Super):
    def actions(self):
        self.method()
class Sub2(Tool):
    def __init__(self):
        self.method = 99

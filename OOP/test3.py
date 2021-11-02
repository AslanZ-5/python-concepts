from test import FirstClass


class ThirdClass(FirstClass):  # Inherit from SecondClass
    def __init__(self, value):  # On "ThirdClass(value)"
        self.data = value

    def __add__(self, other):  # On "self + other"
        return ThirdClass(self.data + other)

    def __str__(self):  # On "print(self)", "str()"

        return '[ThirdClass: %s]' % self.data

    def mul(self, other):  # In-place change: named
        self.data *= other


class SuperList(list):
    def __init__(self, l):
        self.l = list(l)

    def __len__(self):
        return len(self.l)

    def append(self, item):
        return self.l.append(item)


if __name__ == '__main__':
    l1 = SuperList([1, 23, 4, 5, 6])
    l1.append(3333)
    d = ThirdClass(32)



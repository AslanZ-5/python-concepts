class Commuter2:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other

    def __radd__(self, other):
        return self.__add__(other)  # Call __add__ explicity


class Commuter3:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other

    def __radd__(self, other):
        return self + other


class Commuter4:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other

    __radd__ = __add__


a = Commuter4(43)
print(a + 10)
print(a.val)


class Commuter5:  # Propagate class type in results
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        if isinstance(other, Commuter5):  # Type test to avoid object nesting
            other = other.val
        return Commuter5(self.val + other)  # Else + result is another Commuter

    def __radd__(self, other):
        return Commuter5(other + self.val)

    def __str__(self):
        return '<Commuter5: %s>' % self.val

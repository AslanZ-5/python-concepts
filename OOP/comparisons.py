class C:
    data = 19

    def __gt__(self, other):
        return self.data > other

    def __lt__(self, other):
        return self.data < other

    def __bool__(self):
        if self.data < 20:
            return False
        else:
            return True


# x = C()
# print(bool(x))


class C1:
    def __len__(self):
        return 0

x = C1()
print(bool(x))
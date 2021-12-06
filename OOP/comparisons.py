class C:
    data = 33

    def __gt__(self, other):
        return self.data > other

    def __lt__(self, other):
        return self.data < other


x = C()
print(x > 3)
print(x < 333)

class C:
    def __index__(self):
        return 255


x = C()
print(hex(x))
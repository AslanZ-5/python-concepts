class Callee:
    def __call__(self, *args, **kwargs):
        print('Called:', args, kwargs)


class Prod:
    def __init__(self, value):
        self.value = value

    def __call__(self, other):
        return self.value * other


if __name__ == '__main__':
    c = Callee()
    c(32, 1, 6, d=5, f=4)
    x = Prod(50)
    print(x(10))


import random

v = []
for x in range(10):
    v.append(random.randrange(100))
print(v)


def lower(value):
    if value < 50:
        return True
    else:
        return False


f = filter(lower, v)
print(list(f))


# filter types

class Animal:
    name = ''

    def __init__(self, name):
        self.name = name


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)


animals = []

for x in range(1,10+1):
    name = 'object' + str(x)
    if x % 2 == 0:
        animals.append({Cat(name)})
    else:
        animals.append(Dog(name))

# for i in animals:
    # print(i.name)

def cats(v):
    return isinstance(v,Cat)\

def cats(v):
    return isinstance(v,Cat)

for c in list(filter(cats,animals)):
    print(f'Cat : {c.name}')


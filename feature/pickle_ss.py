import pickle



def outline(func):
    def inner(*args, **kwargs):
        print('-' * 20)
        print(f'Function: {func.__name__}')
        func(*args, **kwargs)
        print('-' * 20)

    return inner


class Cat:
    def __init__(self, name, age, info):
        self._name = name
        self._age = age
        self._info = info

    @outline
    def display(self, msg=''):
        print(msg)
        print(f'{self._name} is a {self._age} is years old cat ')
        for k, v in self._info.items():
            print(f'{k} = {v}')

othell = Cat('Othell', 15, dict(color='Black',weight=14,loves='eat'))
othell.display('testing')

#
sc = pickle.dumps(othell)
print(sc)

with open('cat.txt', 'wb')as f:
    pickle.dump(othell,f)


mycat = pickle.loads(sc)
print('from 777777777777777777str')
mycat.display('from str')


with open('cat.txt','rb') as f:
    diskcat = pickle.load(f)
diskcat.display('ddsfdsfsdfsfsfsdfsdfsdf')

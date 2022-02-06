class D:
    def __get__(*args):
        print('get')

    # def __set__(*args):
    #     raise AttributeError('cannot set')


class C:
    a = D()


#
# X = C()
# # X.a
# X.a = 'hellow'
# print(X.a)


class Name:
    """Name descriptor docs"""

    def __get__(self, instance, owner):
        print('fetch...')
        return instance._name

    def __set__(self, instance, value):
        print('change...')
        instance._name = value

    def __delete__(self, instance):
        print('remove...')
        del instance._name


class Person:
    def __init__(self, name):
        self._name = name

    name = Name()


# a = Person('Aslan')
#
# print(a.name)
# a.name = 'aslan zurabov'
# print(Name.__doc__)

class DescState:
    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):
        print('DescState get')
        return self.value * 10

    def __set__(self, instance, value):
        print('DescState set')
        self.value = value
class CalcAttrs:
    X = DescState(2)
    Y = 3
    def __init__(self):
        self.Z = 4
#
# obj = CalcAttrs()
# print(obj.X,obj.Y,obj.Z)
# obj.X = 5
# CalcAttrs.Y = 6
# obj.Z = 7
# print(obj.X,obj.Y,obj.Z)

class InstState:
    def __get__(self, instance, owner):
        print('InstState get')
        return instance._X * 10
    def __set__(self, instance, value):
        print("InstState set")
        instance._X = value

# Client Class
class CalcAttrs2:
    X = InstState()
    Y = 3
    def __init__(self):
        self._X = 2
        self.Z = 4

obj = CalcAttrs2()
print(obj.Z,obj.X,obj.Y)
obj.X = 5
CalcAttrs2.Y = 6
obj.Z = 7
print(obj.Z,obj.X,obj.Y)
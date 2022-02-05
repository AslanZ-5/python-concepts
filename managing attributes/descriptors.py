# class D:
#     def __get__(*args):
#         print('get')
#
#     # def __set__(*args):
#     #     raise AttributeError('cannot set')
#
#
# class C:
#     a = D()
#
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
    def __init__(self,name):
        self._name = name
    name = Name()

a = Person('Aslan')

print(a.name)
a.name = 'aslan zurabov'
print(Name.__doc__)
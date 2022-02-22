class MetaOne(type):
    def __new__(cls, *args, **kwargs):
        print('In MetaOne', *args, **kwargs, sep='\n....')
        return type.__new__(cls, *args, **kwargs)

    def __init__(Class,*args,**kwargs):
        print('In MetaTwo.init:', *args,**kwargs, sep='\n....')
        print('...init class object:', list(Class.__dict__.keys()
                                            ))


class Eggs:
    pass


print('Making class')


class Spam(Eggs, metaclass=MetaOne):
    data = 1

    def meth(self, arg):
        return self.data + arg


print('making instance')
x = Spam()
print('data:', x.data, x.meth(2))


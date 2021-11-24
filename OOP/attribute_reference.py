class Empity:
    def __getattr__(self, item):
        if item == 'age':
            return 232
        else:
            raise AttributeError('ddddd')

    def __setattr__(self, key, value):
        if key == 'name':
            self.__dict__[key] = value
        else:
            raise AttributeError('dsew32')
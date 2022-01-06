class operators:
    def __getattr__(self, item):
        if item == 'age':
            return 40
        else:
            raise AttributeError(item)


x = operators()


class properties(object):
    def getage(self):
        return 40

    age = property(getage, None, None)  # (get,set,del) or user @


c = properties()
print(c.age)


class properties2(object):
    def getage(self):
        return 40

    def setage(self, value):
        print('set age: %s' % value)
        self._age = value
    age = property(getage,setage,None)


xr = properties2
xr.age = 42
print(xr.age)
xr.job = 'trainer'
print(xr.job)
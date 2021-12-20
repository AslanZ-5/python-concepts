class ListInherit:
    """
    Use dir() to collect both instance attrs and names inherited from
    its clsses; Python 3.X shows more names than 2.X because of the
    implied object superclass in the new-style class model; getattr()
    fetches inherited names not in self.__dict__; use __str__, not
    __repr__, or else this loops when printing bound methods!
    """
    def __attrname(self):
        result = ''
        for attr in dir(self):
            if attr[:2] == '__' and attr[-2:] == '__':
                result += '\t%s\n' % attr
            else:
                result += '\t%s=%s\n' % (attr,getattr(self,attr))
            return result

    def __str__(self):
        return '<Instance of %s, address %s:\n%s>' % (
                                self.__class__.__name__,
                                id(self),
                                self.__attrname()
        )

class testt(ListInherit):
    def dd(self):
        print('say hello')

if __name__ == '__main__':
    a = testt()
    print(dir(a))
    print(getattr(a,'dd'))
    # result = ''
    # for attr in dir(a):
    #     if attr[:2] == '__' and attr[-2:] == '__':
    #         result += '\t%s\n' % attr
    #     else:
    #         result += '\t%s=%s\n' % (attr, getattr(a, attr))
    #
    # print(result)



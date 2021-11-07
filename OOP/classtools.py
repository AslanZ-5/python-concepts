class AttrDisplay:
    """
    Provides an inheritable display overload method
    that shows instances with their class names and a
    name=value pair for each attribute stored on the
    instance itself (but not attrs inherited from its classes).
    Can be mixed into any class, and will work
    on any instance.
    """

    def gatherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append(f'{key}={getattr(self, key)}')
        return ', '.join(attrs)

    def __repr__(self):
        return f'{self.__class__.__name__}: {self.gatherAttrs()}'


if __name__ == '__main__':
    class TopTest(AttrDisplay):
        count = 0

        def __init__(self):
            self.attr1 = TopTest.count
            self.attr2 = TopTest.count + 1
            TopTest.count += 2

        def __gatherAttrs(self):
            return 'Spam'
    class SubTest(TopTest):
        pass
    X,Y = TopTest(),SubTest()
    print(X.gatherAttrs())
    print(Y)

import docstr

# print(docstr.__doc__)
# print(docstr.fun.__doc__)
# print(docstr.spam.__doc__)
# print(docstr.spam.method.__doc__)
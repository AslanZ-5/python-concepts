class Wrapper:
    def __init__(self,object):
        self.wrapper = object

    def __getattr__(self, item):
        print(f'Trace {item}')
        return getattr(self.wrapper, item)

a = Wrapper([33,2])

a.append('de3')
a.pop()
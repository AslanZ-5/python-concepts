# Extending Types by Embedding
class Set:
    def __init__(self, value=[]):
        self.data = []
        self.concat(value)

    def intersect(self, other):
        res = []
        for x in self.data:
            if x in other:
                res.append(x)
        return Set(res)

    def union(self, other):
        res = self.data[:]
        for x in other:
            if not x in res:
                res.append(x)
        return Set(res)

    def concat(self, value):
        for x in value:
            if not x in self.data:
                self.data.append(x)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, key):
        return self.data[key]

    def __and__(self, other):
        return self.intersect(other)

    def __or__(self, other):
        return self.union(other)

    def __repr__(self):
        return "Set:" + repr(self.data)

    def __iter__(self):
        return iter(self.data)


x = Set([1, 3, 5, 7])
print(x | Set([1, 4, 6]))
print(x.union(Set([1, 4, 7])))


# Extending types by subclassing
class Mylist(list):
    def __getitem__(self, offset):
        print('(indexing %s at %s)' % (self, offset))
        return list.__getitem__(self, offset-1)
if __name__ == "__main__":
    print(list('abc'))
    x = Mylist('abc')  # __init__ inherited from list
    print(x)    # __repr__ inherited from list
    print(x[1]) # Mylist.__getitem__  Customizes list superclass method
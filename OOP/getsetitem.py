class Indexer:
    data = [5, 6, 7, 8, 9]

    def __getitem__(self, item):
        if isinstance(item,int) and item <= len(self.data)-1:
            return self.data[item]
        elif item.stop <= len(self.data)-1:
            return self.data[item]
        else:
            return 'some error'





a = Indexer()

print(a[1:4])

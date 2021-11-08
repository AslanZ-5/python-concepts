class Indexer:
    data = [5, 6, 7, 8, 9]

    def __getitem__(self, item):
        if isinstance(item, int) and item <= len(self.data) - 1:
            return self.data[item]
        elif item.stop <= len(self.data) - 1:
            return self.data[item]
        else:
            return 'some error'


class StepperIndex:
    def __getitem__(self, item):
        return self.data[item]


x = StepperIndex()
x.data = 'spam'

for i in x:
    print(i, end=' ')

import random


class Lotto:
    def __init__(self):
        self._max = 4


    def __iter__(self):
        for i in range(self._max):
            yield random.randrange(0,100)

    def setMax(self, max):
        self._max = max
    def displayMax(self):
        print(f'the maximum quantity is {self._max}')

l = Lotto()
l.setMax(10)
l.displayMax()
for i in l:
    print(i)
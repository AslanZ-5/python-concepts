class C2:
    a = 32


class C3:
    b = 44


class C1(C2, C3):
    def setname(self, who):
        self.name = who


# i1= C1()
# i2 = C1()
# i1.setname('aslan')
# i2.setname('shamil')
# print(i1.name)

class PlayerCharacter:
    def __init__(self, name):
        self.name = name

    def run(self):
        print('run')
# p1 = PlayerCharacter('aslan')
# print(p1.name)
# p1.run()

class FirstClass(C1):
    def setdata(self,value):
        self.data = value
    def display(self):
        print(self.data)

if __name__ == '__main__':
    x = FirstClass()
    y = FirstClass()



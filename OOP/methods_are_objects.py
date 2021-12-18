class Spam:
    def doit(self,message):
        print(message)


if __name__ == '__main__':
    object1 = Spam()
    t = Spam.doit
    t(object1,'heeeew')


class Eggs:
    def m1(self,n):
        print(n)
    def m2(self):
        x = self.m1
        x(42)

if __name__ == '__main__':
    d = Eggs()
    d.m2()
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



class Selfless:
    def __init__(self,data):
        self.data = data
    def selfless(arg1,arg2):
        return arg1 + arg2
    def normal(self,arg1,arg2):
        return self.data + arg1 + arg2

if __name__ == '__main__':
    print('++++++++++++++')
    X = Selfless(2)
    print(X.normal(3,4))
    print(Selfless.normal(X,4,5))
    print(Selfless.selfless(4,5))
class A:
    def __init__(self):
        print('init A')
    def act(self):
        print('A')


class B:
    def __init__(self):
        super().__init__()
        print('init b')
    def act(self):
        print('B')


class C(A,B):
    def __init__(self):
        super().__init__()
    def act(self):
        super().act()


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
class Chef1(Employee):
    def __init__(self,name):
        super().__init__(name,50000)

class Server1(Employee):
    def __init__(self,name):
        super().__init__(name,40000)

class TwoJobs(Chef1,Server1):
    pass
tom = TwoJobs('tom')

bob = Chef1('bob')
bob2 = Server1('bob2')
print(bob.salary)
print(bob2.salary)
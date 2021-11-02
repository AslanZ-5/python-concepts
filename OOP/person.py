from classtools import AttrDisplay

class Person(AttrDisplay):
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaiseInPercent(self, p):
        self.pay = int(self.pay * (1 + p))

    def __repr__(self):
        return f'Person\'s name "{self.name}" with salary {self.pay} '


if __name__ == '__main__':
    bob = Person('Bob Smith')  # Test the class
    sue = Person('Sue Jones', job='dev', pay=100000)  # Runs __init__ automatically
    # print(bob.name, bob.pay)  # Fetch attached attributes
    # print(sue.name, sue.pay)
    print(sue.lastName())
    print(sue.pay)
    sue.giveRaiseInPercent(.10)
    print(sue)

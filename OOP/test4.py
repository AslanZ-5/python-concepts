from classtools import AttrDisplay


class Person(AttrDisplay):
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    # def __repr__(self):
    #     return '[Person: %s, %s]' % (self.name, self.pay)


class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self,name,'mgr',pay)

    def giveRaise(self, percent, bonus=.10):
        self.person.giveRaise(percent + bonus)

    def __getattr__(self, attr):
        return getattr(self.person, attr)

    # def __repr__(self):
    #     return str(self.person)


class Department:
    def __init__(self, *args):
        self.members = list(args)

    def addMember(self, person):
        self.members.append(person)

    def giveRaises(self, percent):
        for person in self.members:
            person.giveRaise(percent)

    def showAll(self):
        for person in self.members:
            print(person)


if __name__ == "__main__":
    bob = Person('bob Smith', pay=10000)
    sue = Person('Sue Jones', job='dev', pay=10000)
    # tom = Manager('Ton Jones', 54324)
    dev = Department(bob, sue)
    sue.giveRaise(.10)
    print(bob)
    print(sue)
    # print(tom.__dict__.keys())

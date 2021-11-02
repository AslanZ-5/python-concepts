class User:
    def __init__(self,email):
        self.email = email
    def sign_in(self):
        print('logged in ')
    def attack(self):
        print('do nothing')

class Warrior(User):
    def __init__(self,name,power,email):
        super().__init__(email)
        self.name = name
        self.power = power
    def attack(self):
        User.attack(self)
        print(f'atacking with power of {self.power}')



class Archer(User):
    def __init__(self,name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'atacking with arrows: arrows left - {self.num_arrows}')


if __name__ == '__main__':
    w = Warrior('postter',33,'dd@mail.ru')
    a = Archer('adlan',12)
    print(w.email)



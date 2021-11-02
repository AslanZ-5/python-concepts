class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in ')



class Warrior():
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'atacking with power of {self.power}')


class Archer():
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'atacking with arrows: arrows left - {self.num_arrows}')

class Rom(User,Warrior,Archer):
    def __init__(self,name,power,num_arrows,email):
        Warrior.__init__(self,name,power)
        Archer.__init__(self,name,num_arrows)
        User.__init__(self,email)




if __name__ == '__main__':
    w = Rom('aslan',50,34,'z@mail.ru')
    print(w.email)


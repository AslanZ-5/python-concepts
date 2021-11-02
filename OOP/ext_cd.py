import jsonfrom os import pathclass Inventory:    pets = {}    def __init__(self):        pass    def add(self, key, qty):        q = 0        if key in self.pets:            v = self.pets[key]            q = v + qty        else:            q = qty        self.pets[key] = q        print(f'Added {qty} {key}: total = {self.pets[key]}')    def remove(self, key, qty):        q = 0        if key in self.pets:            v = self.pets[key]            q = v - qty        if q<0:            q = 0        self.pets[key] = q        print(f'Removed {qty} {key}: total = {self.pets[key]}')    def display(self):        for key, value in self.pets.items():            print(f'{key} = {value}')    def save(self):        print('Saving Inventory')        with open('inventory.txt', 'w') as f:            json.dump(self.pets,f)        print('Saved')    def load(self):        print('loading inventory')        if not path.exists('inventory.txt'):            print('Skippin, nothing to load')            return        with open('inventory.txt','r') as f:            self.pets = json.load(f)        print('Loaded!!')if __name__ == '__main__':    a = Inventory()    a.add('miki',4)    a.add('miki',2)    a.remove('miki',1)    a.display()    print(a.pets)    a.add('dada',3)    a.save()    a.save()a.load()print(a.pets)
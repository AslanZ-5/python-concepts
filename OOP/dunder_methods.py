class Toy():
    def __init__(self,color,age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name':'aslan',
            'ha_pets':False
        }
    def __str__(self):
        return f'{self.color}'

    def __len__(self):
        return len(self.color)

    def __call__(self):
        return 'This class was called'

    def __getitem__(self, item):
        return self.my_dict[item]


if __name__ == '__main__':
    a = Toy('red',32)
    print(a['name'])
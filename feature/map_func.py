people = ['Matt', 'Bryan', 'Tammy', 'Markus']
print(list(map(len,people )))


firstnames = ('Apple','Choclate','Fudge','Pizza')
lastnames = ('Pie','Cake','Brownies')

def mer(a,b):
    return a + ' ' + b

print(list(map(mer,firstnames,lastnames)))
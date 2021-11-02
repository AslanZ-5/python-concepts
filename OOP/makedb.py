from test4 import Person,Manager
import shelve

bob = Person('bob Smith', pay=10000)
sue = Person('Sue Jones', job='dev', pay=10000)
# tom = Manager('Ton Jones', 54324)
print(bob)
print(sue)
# print(tom)
db = shelve.open('persondb')
for obj in (bob,sue):
    db[obj.name] = obj
db.close()




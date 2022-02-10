from validate_getattribute import CardHolder

bob = CardHolder('1234-3216','Bob Smith',40,'123 main st')
print(bob)
print('\n')
bob.name = 'Bob Q. Smith'
bob.age = 50
bob.acct = '23-45-67-89'
print(bob)
sep = '-' * 45 + '\n'

print(sep + 'EXCEPTION RAISED AND CAUGHT')

try:
    x = 'spam'[99]
except IndexError:
    print('Except run')
else:
    print('else run')
finally:
    print('finally run')
print('after run')

print(sep + 'NO EXCEPTION RAISED AND CAUGHT')

try:
    x = 'spam'[3]
except IndexError:
    print('Except run')
else:
    print('else run')
finally:
    print('finally run')
print('after run')



print(sep + 'EXCEPTION RAISED BUT NOT CAUGHT')

try:
    x = 5 / 0
except IndexError:
    print('Except run')
else:
    print('else run')
finally:
    print('finally run')
print('after run')

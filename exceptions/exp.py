class Found(Exception):
    pass

def sercher():
    if True:
        raise Found()
    else:
        return 1

try:
    sercher()
except Found:
    print('ew')
else:
    print('filure')
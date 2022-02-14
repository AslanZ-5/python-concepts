import sys
import time
force = list if sys.version_info[0] == 3 else (lambda X: X)


class timer:
    def __init__(self, func):
        self.func = func
        self.alltime = 0

    def __call__(self, *args, **kwargs):
        start = time.perf_counter()
        result = self.func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        self.alltime += elapsed
        print('%s: %.10f, %.10f' % (self.func.__name__, elapsed, self.alltime))
        return result


@timer
def listcomp(N):
    return [x * 2 for x in range(N)]


@timer
def mapcall(N):
    return force(map((lambda x: x * 2), range(N)))


result = listcomp(5)
listcomp(2120)
listcomp(22120)
listcomp(22120)
a = listcomp(10000)
print('allTime = %s' % listcomp.alltime)

print('------------------')
result2 = mapcall(55)
mapcall(50000)
mapcall(100000)
mapcall(1111111)
print(result2)
print('allTime = %s' % mapcall.alltime)

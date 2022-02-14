import sys
import time

list = list(range(100000))

def gera():
    r = []
    for n in range(10000000):
        r.append(n)
        time.sleep(0.1)
        print(f'{n:0>10d}')
    return r

def gera_yield():
    for n in range(100):
        yield n
        time.sleep()

list = [x for x in range(10000000)]
list2 = (x for x in range(10000000))

print(sys.getsizeof(list))
print(sys.getsizeof(list2))

gera()
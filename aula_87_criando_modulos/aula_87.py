
import math

PI = math.pi

def dobra_lista(lista):
    return [x * 2 for x in lista]

def multiplica(lista):
    r = 1
    for i in lista:
        r *= i
        return r

lista = [1, 2, 3, 4, 6]

if __name__ == "__main__":
    print(dobra_lista(lista))
    print(multiplica(lista))
    print(PI)
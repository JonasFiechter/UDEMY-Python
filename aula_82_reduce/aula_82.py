from aula_80_map.aula_80_data import *
from functools import reduce

acumula = 0
for item in lista:
    acumula += item

print(acumula)

######################

soma_lista = reduce(lambda ac, i: i + ac, lista, 0)
print(soma_lista)

soma_produtos = reduce(lambda ac, p: p['preço'] + ac, produtos, 0)
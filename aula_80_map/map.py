from aula_80_data import produtos, pessoas, lista

nova_lista = map(lambda x: x * 2, lista)

print(lista)
print(list(nova_lista))

####################################################

nova_lista = [x * 2 for x in lista]

print(lista)
print(list(nova_lista))

#####################################################

def aumenta_preco(p):
    p['preço'] = p['preço'] * 1.05
    return p

precos = map(aumenta_preco, produtos)

for p in list(precos):
    print(p)

######################################################

nomes = map(lambda p: p['nome'], pessoas)

for pessoa in nomes:
    print(pessoa)










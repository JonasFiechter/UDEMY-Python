from aula_80_map.aula_80_data import produtos, pessoas, lista

nova_lista = filter(lambda x: x > 5, lista)
print(list(nova_lista))

###############################################

nova_lista2 = [x for x in lista if x > 5]
print(nova_lista2)

###############################################

produto1 = filter(lambda p: p['preço'] > 10, produtos)

print(list(produto1))
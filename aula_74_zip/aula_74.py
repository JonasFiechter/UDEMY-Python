from itertools import zip_longest, count

indice = count()
cidades = ['São Paulo', 'Belo horizonte', 'Curitiba', 'Quebec']
estados = ['SP', 'MG', 'PR']

cidades_estados = zip_longest(
    estados,
    cidades,
    fillvalue='Desconhecido')

print(list(cidades_estados))

##################################################

cidades_estados = zip(
    indice,
    estados,
    cidades)

print(list(cidades_estados))
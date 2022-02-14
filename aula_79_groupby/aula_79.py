from itertools import groupby

alunos = [
        {'nome': 'Luiz', 'nota': 'A'},
        {'nome': 'Letícia', 'nota': 'B'},
        {'nome': 'Fabiano', 'nota': 'C'},
        {'nome': 'Rose', 'nota': 'D'},
        {'nome': 'Joana', 'nota': 'A'}
]

alunos.sort(key=lambda item: item['nota'])
print(alunos)

alunos_agrupados = groupby(alunos, lambda item: item['nota'])

print(i for i in alunos_agrupados)
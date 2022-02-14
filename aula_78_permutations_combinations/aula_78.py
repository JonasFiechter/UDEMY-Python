"""
Combinations, Permutations and Product - Itertools
Combinação = ORDEM NÃO IMPORTA
Permutação = ORDEM IMPORTA
Ambos não repetem valores únicos
Produto - ORDEM IMPORTA E REPETE VALORES ÚNICOS
"""
from itertools import combinations, permutations, product

pessoas = ['Luiz', 'André', 'Letícia', 'Eduardo', 'Rose', 'Eduardo', 'Fabrício']

for grupo in combinations(pessoas, 3):
    print(grupo)

print()

for grupo in permutations(pessoas, 2):
    print(grupo)

print()

for grupo in product(pessoas, repeat=2):
    print(grupo)

file = open('abc.txt', 'w+')
file.write('Linha 1\n')
file.write('Linha 2\n')

file.seek(0, 0)
print('Lendo linhas: ', file.read())

print('########')

file.seek(0, 0)

for linha in file.readlines():
    print(linha, end='')

file.seek(0, 0)

file.close()

#############################################

try:
    file = open('abc.txt', 'w+')
    file.write('Linha')
    file.seek(0, 0)
    print(file.read())
finally:
    file.close()

#############################################

with open('abc.txt', 'w+') as file:
    file.write('Teste da linha1\n')
    file.write('Teste da linha2\n')
    file.seek(0)
    print(file.read())

#############################################

with open('abc.txt', 'r') as file:
    print(file.read())
    file.seek(0)

with open('abc.txt', 'a+') as file:
    file.write('\nLinha adicional')
    file.seek(0)
    print(file.read())

#############################################
try:
    import os
    os.remove('abc1.txt')
except:
    pass

#############################################

import json
from aula_80_map.aula_80_data import pessoas2

pessoas_json = json.dumps(pessoas2, indent=True)

with open('abc.json', 'w+') as file:
    file.write(pessoas_json)
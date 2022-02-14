# Meta caracteres: . ^ $ * + ? { } [ ] \ | ( )
# |  --->  OU
# .  ---> Qualquer caractere (com exceção da quebra de linha)
# [] ---> Conjunto de caracteres (com range utilizando - ex.: [e-z]xample)
# * 0 ou n
# + 1 ou n
# ? 0 ou 1
# {n}
# {min, max}

# O '?' após o meta caractere '*' faz com que a expressão nao funcione no formato greedy 'guloso'

import re

text = '''
<p>Frase 1</p> <p>Frase 2</p> <p>Frase 3</p> <div>Frase 4</div>
'''

print(re.findall(r'<[pdiv]{1,3}>.*<\/[pdiv]{1,3}>', text,))
print(re.findall(r'<[pdiv]{1,3}>.*?<\/[pdiv]{1,3}>', text,))
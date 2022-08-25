# Formatando valores com modificadores

"""

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(NÚMERO)f - Quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

> - ESQUERDA
< - DIREITA
^ - CENTRO

"""
entry1 = int(input('Place any number: '))
entry2 = int(input('Place another number: '))

var_01 = entry1 * 500 + entry2
var_02 = entry2 * 600 - var_01

print(f'{var_01:.2}')
print(f'{var_02:0>10d}')
print(f'{var_02:0>10d}')
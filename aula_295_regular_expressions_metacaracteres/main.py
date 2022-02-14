# Meta caracteres: . ^ $ * + ? { } [ ] \ | ( )
# |  --->  OU
# .  ---> Qualquer caractere (com exceção da quebra de linha)
# [] ---> Conjunto de caracteres (com range utilizando - ex.: [e-z]xample)

import re

text = '''
John brought flower from his loved girfriend on january 10 of 1970.
Her name was Maria

It was an exelent year at John's life, he had 5 childrens... And Maria his wife still making
those delicious cheese breads at afternoon
'''

print(re.findall(r'John|Maria', text, flags=re.I))
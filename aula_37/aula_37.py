# for em Python
# Iterando strings com for
# Função range(start=0, stop, step=1)

texto = 'Python'
t_texto = len(texto)

for n in texto:
    print(f'{n}')

print('')

for n in range(len(texto) - 1, -1, -1):
    print(f'{texto[n]}')

cnpj_temp = '04252011000110'

regressive = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
lista_temp = []
soma = 0
for n in range(len(first_check)):  # ver1
    lista_temp.append(first_check[n] * int(cnpj_temp[n]))
for i in lista_temp:
    soma += i
ver_digit = 11 - (soma % 11)

lista_temp = [regressive[n] * int(cnpj_temp[n]) for n in range(12)]
print(lista_temp)
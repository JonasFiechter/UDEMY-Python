def remover_caracteres(cnpj):
    cnpj = cnpj.replace('/', '')
    cnpj = cnpj.replace('.', '')
    cnpj = cnpj.replace('-', '')
    return cnpj


def verifica_digitos(regressive, cnpj_temp, digit, x=0, y=12):
    lista_temp = [regressive[n + x] * int(cnpj_temp[n]) for n in range(y)]
    if 11 - (sum(lista_temp) % 11) > 9:
        digit.append('0')
    else:
        digit.append(str(11 - (sum(lista_temp) % 11)))
    return digit


def valida(cnpj):
    cnpj_temp = remover_caracteres(cnpj)
    digit = []
    regressive = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    cnpj_temp = list(cnpj_temp)

    verifica_digitos(regressive=regressive, cnpj_temp=cnpj_temp, digit=digit, x=1, y=12)
    verifica_digitos(regressive=regressive, cnpj_temp=cnpj_temp, digit=digit, y=13)

    if cnpj_temp[12:] == digit:
        return True
    else:
        return False


def main():
    cnpj = input('Digite um CNPJ: ')
    if valida(cnpj=cnpj):
        print('Válido')
        return True
    else:
        print('Inválido')
        return False


if __name__ == '__main__':
    main()

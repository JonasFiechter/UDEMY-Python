import random
import validador_cnpj


def gerador():
    run = True
    while run:
        cnpj = [random.randrange(9) for x in range(8)]
        cnpj1 = ''
        for x in cnpj:
            cnpj1 += str(x)
        cnpj1 = f'{cnpj1[:2]}.{cnpj1[2:5]}.{cnpj1[4:7]}/0001-{random.randrange(99)}'
        cnpj = cnpj1
        if validador_cnpj.valida(cnpj=cnpj):
            return cnpj


def main():
    entry = input('Digite "CNPJ" para gerar um CNPJ ou "Lista" para gerar uma lista: ').upper()
    if entry == 'CNPJ':
        cnpj = gerador()
        print(cnpj)
        return cnpj
    if entry == 'LISTA':
        n_entry = int(input("Digite o numero de CNPJ's para gerar: "))
        lista_cnpj = [gerador() for cnpj in range(n_entry)]
        print(lista_cnpj)
        return lista_cnpj


if __name__ == '__main__':
    main()

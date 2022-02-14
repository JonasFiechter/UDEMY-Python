def converte_numero(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
        except ValueError:
            pass

numero = converte_numero(input('Digite um numero: '))

while True:
    if numero is not None:
        print(numero * 5)
        break
    else:
        print('Isso não é um número')
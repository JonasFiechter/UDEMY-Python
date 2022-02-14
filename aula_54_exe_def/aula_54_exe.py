# crie uma função que exibe uma saudacao com os parametros saudacao e nome.

def _01(var_1, var_2):
    print(f'{var_1} {var_2}')

# crie uma funcao que recebe 3 numeros como parametros e exiba a soma entre eles.

def _02(a, b, c):
    print(a + b + c)

# crie uma funcao que receba 2 numeros. o primeiro e um valor e o segundo um percentual.
# retorne o valor do primeiro numero somado ao percentual do mesmo.

def _03(a, b):
    return a + (a * (b / 100))

# fizz buzz. se o parametro da funcao for divisivel por 3, retorne fizz, se o parametro
# da funcao for divisivel por 5 retorne buzz, se o parametro da funcao for divisivel por 5 e por 3,
# return fizzbuzz caso contrario # retorne o numero enviado.

def _04(a):
    div_03 = a % 3
    div_05 = a % 5

    if div_03 == 0 and div_05 == 0:
        return 'fizzbuzz'

    elif div_03 == 0:
        return 'fizz'

    elif div_05 ==0:
        return 'buzz'

    else:
        return a
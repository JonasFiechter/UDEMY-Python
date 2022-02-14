
    #Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou ímpar,
    #Caso o usuário não digite um número inteiro, informe que o número não é um número inteiro.


    #Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada. Ex.
    #Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.


    #Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva
    #'seu nome é normal'; maior que 6 escreva 'seu nome é muito grande'.


def program_01():
    entry = input('Place a number: ')
    execute = True

    try:
        converted_entry = int(entry)
        print(converted_entry)
    except:
        print('This is not an integer number!')
        execute = False

    if execute:
        division_re = converted_entry % 2
        if division_re > 0:
            print(f'The number {entry} is odd')
        else:
            print(f'The number {entry} is even')

def program_02():
    entry = int(input('Place actual time: '))
    entry2 = int(input('Place actual minute: '))

    if entry >= 18:
        print(f'Boa noite {entry}-{entry2}')
    elif entry >= 12 and entry < 18:
        print(f'Boa tarde {entry}-{entry2}')
    else:
        print(f'Bom dia {entry}-{entry2}')

def program_03():
    entry = input('Place your name: ')
    if len(entry) <= 4:
        print('Your name is normal')
    else:
        print('Your name is big')
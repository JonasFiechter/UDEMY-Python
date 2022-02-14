try:
    print(a)
except:
    pass

try:
    print(a)
except NameError as erro:
    print('Erro:', erro)
except IndexError as erro:
    print('Erro de índice.')
except KeyError as erro:
    print('Erro de chave.')
except Exception as erro:
    print('Erro inesperado')
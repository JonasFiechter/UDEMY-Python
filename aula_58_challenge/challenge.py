# crie uma funcao1 que recebe uma funcao2 como parametro e retorne o valor da funcao2 executada.

def func_01(func_02):
    return func_02()

def func_02():
    return 'Test func_02'

# crie uma funcao1 que recebe uma funcao2 como parametro e retorne o valor da funcao2 executada.
# faca a funcao1 executar duas funcoes que recebam um numero diferente de argumentos.

def func_001(func_002):
    return func_002(), list(func_003('23', 'theodore', 45))

def func_002():
    return 'Test func_002'

def func_003(*args):
    return(args)
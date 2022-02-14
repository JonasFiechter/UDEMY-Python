from contextlib import contextmanager


class Arquivo:
    def __init__(self, arquivo, modo):  # Gerenciador de contexto
        print(f'INIT')
        self.arquivo = open(arquivo, modo)

    def __enter__(self):
        print(f'entrou na classe')
        return self.arquivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('saiu da classe')
        self.arquivo.close()


with Arquivo('abc.txt', 'w') as arquivo:
    arquivo.write('Alguma coisa')


@contextmanager
def abrir(arquivo, modo):
    try:
        arquivo = open(arquivo, modo)
        yield arquivo
    finally:
        arquivo.close()


with abrir('abc.txt', 'w+') as arquivo:
    arquivo.write('Linha 2')
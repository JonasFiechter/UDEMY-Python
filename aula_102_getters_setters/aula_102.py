class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        self.tag = 'Cloathing'

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor.title()

    # getter
    @property
    def preco(self):
        return self._preco

    # setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))

        self._preco = valor

p1 = Produto('camiseta', 50)
p1.desconto(15)
print(p1.nome, f'R${p1.preco:.2f}')

p2 = Produto('CANECA', 'R$15')
p2.desconto(10)
print(f'{p2.preco:.2f} {p2.nome}')

print(p1.tag)
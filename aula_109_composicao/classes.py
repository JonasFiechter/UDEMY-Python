class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def insere_endereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))

    def lista_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.estado, endereco.cidade)

    def __del__(self):
        print(f'{self.nome} "Deleted"')

class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado
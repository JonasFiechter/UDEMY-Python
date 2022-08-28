class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self, fala=False):
        print(f'{self.nomeclasse} {self.nome} falando...')


class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse} {self.nome} está comprando...')


class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nomeclasse} {self.nome} está estudando...')


class ClienteVIP(Cliente):
    def __init__(self, nome, idade, sobrenome):
        Pessoa.__init__(self, nome, idade)
        self.sobrenome = sobrenome

    def falar(self):
        Pessoa.falar(self)
        Cliente.falar(self)
from datetime import *

class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def falar(self, fala):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo.')
            return
        else:
            print(f'{self.nome} diz: {fala}')

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo.')
            return

        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return
        else:
            print(f'{self.nome} parou de comer.')
            self.comendo = False

    def ano_nascimento(self):
        print(f'{self.nome} nasceu em {self.ano_atual - self.idade}')
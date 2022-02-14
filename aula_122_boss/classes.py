from abc import ABC, abstractmethod


class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        self._idade = idade


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.conta = ''

    def criar_conta(self, conta):
        self.conta = conta


class Conta:
    def __init__(self, n_conta, n_agencia, saldo):
        self.n_conta = n_conta
        self.n_agencia = n_agencia
        self.saldo = saldo

    @abstractmethod
    def sacar(self, valor):
        pass

    @abstractmethod
    def depositar(self, valor):
        pass


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if valor < self.saldo:
            print('Saldo insuficiente')
            return
        self.saldo += valor
        print(f'Valor do saque: {valor}'
              f'\nSaldo: {self.saldo}')

    def depositar(self, valor):
        self.saldo -= valor
        print(f'Valor depositado: {valor}'
              f'\nSaldo: {self.saldo}')


class ContaCorrente(Conta):
    def __init__(self, conta, agencia, saldo, limite):
        super().__init__(conta, agencia, saldo)
        self.limite = limite

    def sacar(self, valor):
        if valor > self.saldo + self.limite:
            print('Saldo insuficiente')
            return
        self.saldo -= valor
        print(f'Valor do saque: {valor}'
              f'\nSaldo: {self.saldo}')

    def depositar(self, valor):
        self.saldo += valor
        print(f'Valor depositado: {valor}'
              f'\nSaldo: {self.saldo}')


class Banco:
    pass
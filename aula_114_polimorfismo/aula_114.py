"""
Polimorfismo é o princípio que permite que classes derivadas de uma mesma superclasse tenham
métodos iguais (de mesma assinatura) mas comportamentos diferentes.
Mesma assinatura = Mesma quantidade e tipo de parâmetros
"""

from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def do(self, action): pass

class B(A):
    def do(self, action):
        print(f'A is {action}')

class C(A):
    def do(self, action):
        print(f'C is {action}')
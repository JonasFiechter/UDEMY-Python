"""
Especificar os tipos de objetos a serem criados usando uma instância-protótipo e criar novos
objetos pela cópia desse protótipo

Quais objetos são copiados com o sinal de atribuição?

Método deepcopy python
"""
from __future__ import annotations  # Esta importação evita que seja necessário escrever
from typing import List             # a classe antes de a utilizar como typehinting
from copy import deepcopy


class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.addresses: List = []
    
    def add_address(self, address):
        street, number = address.street, address.number  #foi possível extrair valores da instancia da classe com desempacotamento
        self.addresses.append(street)
        self.addresses.append(number)


class Address:
    def __init__(self, street, number):
        self.street = street
        self.number = number


if __name__ == '__main__':
    loth = Person('Loth', 'Gogariuxa')
    loth_address = Address('Gothic ave.', '233')
    loth.add_address(loth_address)

    loths_brother = deepcopy(loth)
    loths_brother.firstname = 'John'

  
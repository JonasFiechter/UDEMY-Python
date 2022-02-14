"""
Monostate (ou Borg) - É uma variação de SINGLETON proposto por Alex Martelli que tem
a intenção de garantir que o estado do objeto seja igual para todas as instâncias.

__dict__ retorna todos os elementos de uma classe
__str__ determina algum retorno para quando a classe for instanciada
"""

class StringReprMixin:
    def __str__(self):
        return (f'SOME NAME FOR CLASS example:'
               f'\n{self.__class__.__name__} -> {self.__dict__}')

    def __repr__(self):
        return self.__str__()
    

class A(StringReprMixin):
    def __init__(self):
        self.example = True
        self.x = 10
        self.y = 20


class MonoStateSimple(StringReprMixin):
    _state = {
        'x': 10,
        'y': 20,
        'z': -50,
    }

    def __init__(self):
        self.__dict__ = self._state


var1 = MonoStateSimple()
print(var1)
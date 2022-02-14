selffrom eletronico import *
from log import LogMixin


class Smartphone(Eletronico, LogMixin):
    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False

    def conectar(self):
        if not self._ligado:
            info = f'{self._nome} não está ligado'
            self.log_info(info)
            print(info)
            return

        if self._conectado:
            erro = f'{self._nome} já está conectado'
            LogMixin.log_error(self, erro)
            print(erro)
            return

        self._conectado = True
        print(f'{self._nome} está ligando...')

    def desconectar(self):
        if not self._conectado:
            print(f'{self._nome} não está desconectado')
        self._conectado = False

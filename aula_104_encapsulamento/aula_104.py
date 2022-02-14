"""
public, protected, private
_ private/protected (public_)
__ private

"""


class BaseDeDados:
    def __init__(self):
        self.dados = {}

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.dados:
            self.dados['clientes'] = {id: nome}
        else:
            self.dados['clientes'].update({id: nome})

    def lista_clientes(self):
        try:
            for id, nome in self.dados['clientes'].items():
                print(id, nome)
        except:
            print('There is no data in dictionary')

    def apaga_clientes(self, id):
        del self.dados['clientes'][id]


bd = BaseDeDados()
print(bd.dados)

bd.lista_clientes()

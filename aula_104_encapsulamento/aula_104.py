"""
public, protected, private
_ private/protected (public_)
__ private

"""


class BaseDeDados:
    def __init__(self):
        self.dados = {}

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.dados.keys():
            self.dados['clientes'] = {id: nome}
        else:
            self.dados['clientes'].update({id: nome})

    def lista_clientes(self):
        try:
            for key, value in self.dados['clientes'].items():
                print(key, value)
        except:
            print('There is no data in dictionary')

    def apaga_clientes(self, id):
        del self.dados['clientes'][id]


bd = BaseDeDados()
bd.inserir_cliente(0, 'Ammy')
bd.inserir_cliente(1, 'Atga')
bd.inserir_cliente(2, 'Hras')
bd.inserir_cliente(3, 'Utya')

bd.lista_clientes()

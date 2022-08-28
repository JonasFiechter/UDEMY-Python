from classes import Cliente, Endereco

cliente1 = Cliente('John', 32)
cliente1.insere_endereco('Washington', 'BC')
cliente1.lista_enderecos()
del cliente1

cliente2 = Cliente('Jack', 22)
cliente2.inserere_endereco('Rio', 'RJ')


cliente2.lista_enderecos()
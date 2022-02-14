from classes import CarrinhoDeCompras, Produto

carrinho_1 = CarrinhoDeCompras()

p1 = Produto('Chess', 39)
p2 = Produto('Test1', 12)
p3 = Produto('Test2', 440)

carrinho_1.inserir_produto(p1)
carrinho_1.inserir_produto(p1)
carrinho_1.inserir_produto(p2)
carrinho_1.inserir_produto(p3)

CarrinhoDeCompras.lista_produtos(carrinho_1)
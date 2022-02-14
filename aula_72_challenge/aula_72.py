carrinho = []

carrinho.append(('produto 1', 30))
carrinho.append(('produto 2', 50))
carrinho.append(('produto 3', 40))

total = [carrinho[n][1] for n, l in enumerate(carrinho)]

print(sum(total))

##############################################################

carrinho = []

carrinho.append(('produto 1', 30))
carrinho.append(('produto 2', 50))
carrinho.append(('produto 3', 40))

total = sum([float(y) for x, y in carrinho])

print(total)
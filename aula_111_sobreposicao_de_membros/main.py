from classes import *

"""
Associacao = USA | Agregacao = TEM | Composicao = É dono | Heranca = É

"""

p1 = Aluno('Maria', 20)
p1.falar()
p1.estudar()
print(p1.nome, p1.idade)

c1 = Cliente('Jack', 45)
print(c1.nome, c1.idade)
c1.falar('Olá')

a1 = Aluno('Boris', 120)
a1.falar()
a1.estudar()

c2 = ClienteVIP('Marui', 25, 'Lombard')
c2.falar()

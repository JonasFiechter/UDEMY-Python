"""
Boss

    Exercício com Abstração, Herança, Encapsulamento e Polimorfismo.
Criar um sistema bancário (extremamente simples) que tenha clientes, contas e um banco. A ideia é que o cliente
tenha uma conta (poupança ou corrente) e que possa sacar/depositar nesta conta. Contas corrente tem um limite
extra. Banco tem clientes e contas.

Tips:
Criar classe Cliente que herda da classe Pessoa(herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e polimorfismo - as subclasses que
    implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável por autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clientes(Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
"""
from classes import Cliente, ContaCorrente, ContaPoupanca

p1 = Cliente('Jones', 12)

conta1 = ContaCorrente(123, 23, 30, 100)

p1.criar_conta(conta1)

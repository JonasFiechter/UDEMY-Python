from aula_113_classes_abstratas.classes.conta_poupanca import ContaPoupanca
from aula_113_classes_abstratas.classes.conta_corrente import ContaCorrente

cp = ContaPoupanca(1111, 222, 90)

cp.depositar(20)

cc = ContaCorrente(1000, 111, 120)
cc.depositar(100)
nome = 'Jorginho'
idade = 20
altura = 1.79
e_maior = idade > 18
peso = 80
imc = peso / (altura ** 2)

if e_maior:
    e_maior = 'de maior'
else:
    e_maior = 'de menor'

print(nome, 'é', e_maior, 'tem', idade, 'anos de idade, e seu IMC é:', imc)
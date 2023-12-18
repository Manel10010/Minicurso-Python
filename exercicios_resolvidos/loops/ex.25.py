'''
Exercício Python 25: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte 
ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada 
valor serão entregues.
OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e moedas de R$1.
'''
valor = int(input('Valor a ser sacado: R$'))
nota_50 = 0
nota_20 = 0
nota_10 = 0
moeda_1 = 0
while valor>=50:
    valor -= 50
    nota_50 += 1
while valor>=20:
    valor -= 20
    nota_20 += 1
while valor >= 10:
    valor -= 10
    nota_10 += 1
while valor >= 1:
    valor -= 1
    moeda_1 += 1

print(f'O valor de R${valor:.2f} foi sacado em: ')
print(f'{nota_50} notas de R$50, {nota_20} notas de R$20, {nota_10} notas de R$10, {moeda_1} moedas de R$1')
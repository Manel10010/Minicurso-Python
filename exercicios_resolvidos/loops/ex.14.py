'''
Exercício Python 14: Desenvolva um programa que leia a idade de 4 pessoas. No final do programa 
mostre a média de idade do grupo.
'''
total = 0
for x in range(4):
    idade = float(input('Idade: '))
    total += idade

print(f'A média da idade do grupo foi de {(total/4):.0f} anos')
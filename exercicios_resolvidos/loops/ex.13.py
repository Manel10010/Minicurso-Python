'''
Exercício Python 13: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual 
foi o maior e o menor peso lidos.
'''

for x in range(5):
    peso = float(input('Peso[Kg]: '))
    if x == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso foi {maior}kg')
print(f'O menor peso foi {menor}kg')

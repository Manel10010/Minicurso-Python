'''
Exercício Python 29: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. 
No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.
'''
n1 = int(input('Valor: '))
n2 = int(input('Valor: '))
n3 = int(input('Valor: '))
n4 = int(input('Valor: '))
tupla = (n1, n2, n3, n4)
contador_9 = 0
for x in tupla:
    if x == 9:
        contador_9 += 1
for x in range(0, len(tupla)):
    if tupla[x] == 3:
        print(f'A primeira posição em que o 3 apareceu foi: {x}')
        break
print(f'O valor 9 apareceu {contador_9} vezes.')
print('Valores pares:')
for x in tupla:
    if x%2 == 0:
        print(x, end=' ')
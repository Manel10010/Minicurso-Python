'''
Exercício Python 37: Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores 
ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
'''
lista = []
lista_par = []
lista_impar = []
for x in range(0, 5):
    num = int(input('Digite um valor: '))
    lista.append(num)
    if num%2 == 0:
        lista_par.append(num)
    else:
        lista_impar.append(num)

print(f'Lista: {lista}')
print(f'Lista com os pares: {lista_par}')
print(f'Lista com os ímpares: {lista_impar}')
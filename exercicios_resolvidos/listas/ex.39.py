'''
Exercício Python 39: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
No final, mostre:

A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''

lista = []
lista_dados = []
lista_pesados = []
lista_leves = []
qntd_cadastradas = 0
for x in range(0, 5): #Adcionando os valores em forma de lista, dentro da lista principal
    nome = input('Nome: ')
    peso = float(input('Peso: '))
    if x == 0:
        maior_peso = peso
        menor_peso = peso
    else: #Verificando maior peso
        if peso > maior_peso:
            maior_peso = peso
        elif peso < menor_peso:
            menor_peso = peso
    lista_dados.append(nome)
    lista_dados.append(peso)
    lista.append(lista_dados[:])
    lista_dados.clear()
    qntd_cadastradas += 1

for x in lista: #Salvando os mais pesados
    if x[1] == maior_peso:
        lista_pesados.append(x[0])
    elif x[1] == menor_peso:
        lista_leves.append(x[0])

print(maior_peso)
print(menor_peso)
print(f'Ao todo foram cadastradas {qntd_cadastradas} pessoas.')
print(f'Lista dos mais pesados: {lista_pesados}')
print(f'Lista dos mais leves: {lista_leves}')
    
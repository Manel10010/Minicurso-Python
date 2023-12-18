'''
Exercício Python 41: Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores 
lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
'''
matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, len(matrix)): #Passando na linha
    for coluna in range(0, len(matrix[0])): #Passando na coluna
        num = int(input(f'Digite o valor para posição [{linha},{coluna}]: '))
        matrix[linha][coluna] = num #Adicionando valor a posição linha/coluna

for l in range(0, len(matrix)):
    for c in range(0, len(matrix[0])):
        print(f'[{matrix[l][c]:^5}]', end='') #Pritando com end=''
    print() #utilizado para fzr o pulo entre linhas
'''
Exercício Python 30: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos 
preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
'''

tupla = ('Feijão', 10.50, 'Macarrão', 7.50, 'Manteiga', 10.50, 'Queijo', 12.50, 'Arroz', 6.50)
print('-=-=-=-=-=- TABELA DAS COMPRAS -=-=-=-=-=-')
print('ITEM                                |PREÇO')
print('------------------------------------------')
for x in range(0, len(tupla)):
    if x%2 == 0:
        print(f'{tupla[x]:.<36}', end='')
    else:
        print(f'|{tupla[x]}', end='\n')
print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
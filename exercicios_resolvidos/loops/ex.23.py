'''
Exercício Python 23: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, 
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.
'''
maiores = 0
homens = 0
mulher_m20 = 0
r = 'S'
while r in 'Ss':
    idade = float(input('Idade: '))
    sexo = input('Digite seu sexo[M/F]: ')
    if idade > 18:
        maiores += 1
    if sexo in 'Mm':
        homens += 1
    if sexo in 'Ff' and idade < 20:
        mulher_m20 += 1
    r = input('Deseja continuar?[S/N]: ')

print(f'Ao todo foram {maiores} pessoas tem mais de 18 anos')
print(f'Ao todo {homens} homens foram cadastrados.')
print(f'Ao todo {mulher_m20} mulheres cadastradas tem menos de 20 anos.')
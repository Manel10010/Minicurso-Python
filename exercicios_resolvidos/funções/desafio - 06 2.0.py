"""
Crie uma função que recebe duas notas de um aluno e:
a) Calcula e mostra sua média
b) Mostra o STATUS do aluno, Média menor que 5 - REPROVADO, Média acima de 5 mas abaixo de 7 - RECUPERAÇÃO - Média maior que 7 - APROVADO
"""
def status_aluno(n1, n2):
    média = (n1 + n2)/2
    print(f'Sua média foi {média}')
    print('STATUS: ', end='')
    if média < 5:
        print('REPROVADO')
    elif 7 > média >= 5:
        print('RECUPERAÇÃO')
    else:
        print('APROVADO')

#Os nomes das variáveis que irão ser passadas ao invocar a função, não precisam ser iguais aos definidos nos parâmetros da função!
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
status_aluno(nota1, nota2)
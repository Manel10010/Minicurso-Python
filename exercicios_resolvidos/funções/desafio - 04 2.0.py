"""
Crie uma função chamada radar que recebe a velocidade de um carro e o limite de velocidade. 
Se a velocidade exceder o limite, a função aplica uma multa ao motorista. 
O cálculo da multa é realizado pela diferença entre a velocidade e o limite, multiplicada por 7. 
Após o cálculo, a função exibe uma mensagem informando sobre a multa com a velocidade limite ultrapassada e o valor a ser pago. 
Se a velocidade não exceder o limite, a função retorna a mensagem "Você está dentro dos parâmetros da lei, tenha um bom dia!"
"""

def radar(vel, limite):
    if vel > limite:
        multa = (vel - limite) * 7
        print(f'Você foi multado por está acima do limite de {limite}km/h')
        print(f'Valor a ser pago: R${multa:.2f}')
    else:
        print('Você está dentro dos parâmetros da lei, tenha um bom dia!')


#Com a adição da função fica bem mais fácil alterar valores, e definir novas condições.
vel = float(input('Velocidade[Km/h]: '))
radar(vel, 80) #Limite de 80km/h
radar(vel, 70) #Limite de 70km/h
radar(vel, 60) #Limite de 60km/h
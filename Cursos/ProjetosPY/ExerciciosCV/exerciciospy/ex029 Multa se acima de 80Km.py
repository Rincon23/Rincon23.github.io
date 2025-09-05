from math import trunc
vel = float(input('Qual a velocidade do carro: '))

if vel <= 80:
    print('Você não tomou multa! Pode passar!')
else:
    print('Você foi multado!')
    print('Valor da Multa: {}'.format(trunc(vel-80)*7))

km = float(input('Qual é a distância da viagem? '))

if km <= 200:
    print('Você pagará R$0,50 por km. Calculado: R${}'.format(km*0.5))
else:
    print('Você pagará R$0,45 por km. Calculado: R${}'.format(km*0.45))
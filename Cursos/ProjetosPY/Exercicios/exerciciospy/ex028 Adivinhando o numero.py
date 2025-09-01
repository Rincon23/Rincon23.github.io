from random import randint

n1 = randint(1,5)
n2 = int(input('Escolha um numero de 1 a 5: '))

if n1 == n2:
    print('Você ganhou o computador escolheu o {}!'.format(n1))
else:
    print('Você Perdeu o computador escolheu o numero {} e você escolheu o {}'.format(n1,n2))
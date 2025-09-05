from random import randint

n1 = 0
ganho = 0

while True:
    n1 = randint(1,2)
    n2 = int(input('Escolha um numero: '))
    escolha = input('Você deseja par ou impar? [p/i] ')

    if (escolha == 'p' and (n1+n2)%2 == 0) or (escolha == 'i' and (n1+n2)%2 != 0):
        ganho += 1
        print(f'Você ganhou, jogue novamente! \nEle jogou o numero {n1}')
    else:
        print(f'Você perdeu!\nEle jogou o numero {n1}')
        print(f'Partidas ganhas {ganho}')
        break
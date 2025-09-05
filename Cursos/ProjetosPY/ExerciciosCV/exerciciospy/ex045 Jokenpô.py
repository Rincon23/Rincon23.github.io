from random import choice

jog1 = choice(['Pedra', 'Papel', 'Tesoura'])

cond = int(input("""
Digite o numero da jogada:
                 
1. Pedra
2. Papel
3. Tesoura
"""))

if cond >=1 or cond<=3:

    print('Jogada da maquina: ',jog1)

    if cond == 1:
        jog2 = 'Pedra'
    elif cond == 2:
        jog2 = 'Papel'
    else: 
        jog2 = 'Tesoura'
    
    print('Sua Jogada: ',jog2)

    if jog1 == jog2:
        print('Empate!')

    elif jog1 == 'Pedra':
        if jog2 == 'Tesoura':
            print('Você Perdeu!')
        else:
            print('Você ganhou!') 

    elif jog1 == 'Tesoura':
        if jog2 == 'Papel':
            print('Você Perdeu!')
        else:
            print('Você ganhou!')  

    elif jog1 == 'Papel':
        if jog2 == 'Pedra':
            print('Você Perdeu!')
        else:
            print('Você ganhou!')    
else:
    print('Jogada invalida!') 


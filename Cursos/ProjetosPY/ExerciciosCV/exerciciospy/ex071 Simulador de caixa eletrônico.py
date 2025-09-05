saque = int(input('Quanto quer sacar? '))
troco50 = 0
troco20 = 0
troco10 = 0
troco1 = 0

if saque > 50:
    print('Total de', end=' ')
    troco50 = saque//50
    print(f'{troco50} cédulas de 50')
    saque -= troco50*50

if saque > 20:
    print('Total de', end=' ')
    troco20 = saque//20
    print(f'{troco20} cédulas de 20')
    saque -= troco20*20

if saque > 10:
    print('Total de', end=' ')
    troco10 = saque//10
    print(f'{troco10} cédulas de 10')
    saque -= troco10*10

if saque > 1:
    print('Total de', end=' ')
    troco1 = saque//1
    print(f'{troco1} cédulas de 1')
    saque -= troco1
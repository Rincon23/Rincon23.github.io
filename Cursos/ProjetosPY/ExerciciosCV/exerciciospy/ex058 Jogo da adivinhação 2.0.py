from random import randint

n1 = 0
n2 = int(input('Escolha um numero de 1 a 10: '))
c = 0

while n1 != n2:
    n1 = randint(1,10)
    c += 1
    print(n1)
print('Foram necessarios {} palpites!'.format(c))
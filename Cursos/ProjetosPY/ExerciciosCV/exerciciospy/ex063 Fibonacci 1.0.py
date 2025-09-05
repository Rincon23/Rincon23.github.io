n = int(input('Quantos termos de fibonacci? '))
i=0
fibo1 = 0
fibo2 = 1
resul = 0

while i != n-2:

    resul = fibo1 + fibo2
    if i == 0:
        print('{}-{}-{}'.format(fibo1,fibo2,resul), end='')
    else:
        print('-{}'.format(resul), end='')
    
    fibo1 = fibo2
    fibo2 = resul

    i += 1
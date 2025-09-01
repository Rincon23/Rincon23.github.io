n = int(input('Digite um numero: '))
primeiro = n 
fac = 0
print('{}! ='.format(n), end=' ')

while n != 0:

    if n != 1:
        print('{}*'.format(n), end='')
    else:
        print('{}'.format(n), end='')
    
    if n == primeiro:
        fac += n*(n-1)
    elif n == 1:
        fac = fac
    else:
        fac *= (n-1)

    n -=1

print(' = {}'.format(fac))
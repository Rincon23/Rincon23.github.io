

while True:
    n = int(input('Valor para fazer a tabuada: '))
    
    if n < 0:
        break

    for i in range(1,11):
        print('{} * {} = {}'.format(n,i,n*i))

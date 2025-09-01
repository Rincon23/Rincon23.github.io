a = float(input('Digite o 1º lado: '))
b = float(input('Digite o 2º lado: '))
c = float(input('Digite o 3º lado: '))

if a+b > c and a+c > b and b+c > a:
    print('Essas 3 retas formam um triângulo!')
else:
    print('Essas 3 retas não formam um triângulo!')
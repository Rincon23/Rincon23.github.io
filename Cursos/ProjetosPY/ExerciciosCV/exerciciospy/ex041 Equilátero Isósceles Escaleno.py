a = float(input('Digite o 1º lado: '))
b = float(input('Digite o 2º lado: '))
c = float(input('Digite o 3º lado: '))


if a+b > c and a+c > b and b+c > a:
    print('Essas 3 retas formam um triângulo!')
    if a == b and a == c and b == c:
        print('Formam um triangulo Equilátero!')
    elif a == b or a == c or b==c:
        print('Formam um triangulo Isóceles!')
    else:
        print('Formam um triangulo Escaleno!')
else:
    print('Essas 3 retas não formam um triângulo!')
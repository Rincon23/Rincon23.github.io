p = float(input('Digite o peso: '))
a = float(input('Digite a altura: '))
imc = p/a**2

if p > 0 and a > 0:
    print('O IMC é igual a {}!'.format(imc))
    if imc < 18.5:
        print('Abaixo do peso!')
    elif imc <=25:
        print('Peso ideal!')
    elif imc <=30:
        print('Sobrepeso!')
    elif imc > 40:
        print('Obesidade Mórbida')
else:
    print('Peso ou altura invalidos!')

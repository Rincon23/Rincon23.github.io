vl = float(input('Digite o valor do produto: '))
cond = int(input("""
Digite a condição de pagamento:
                 
1. À vista
2. À vista no cartão
3. 2x no cartão
4. 3x ou mais no cartão
"""))

if cond >=1 or cond<=4:
    if cond == 1:
        print('O valor será de: {}'.format(-vl*10/100+vl))
    if cond == 2:
        print('O valor será de: {}'.format(-vl*5/100+vl))
    if cond == 3:
        print('O valor será de: {}'.format(vl))
    if cond == 4:
        print('O valor será de: {}'.format(vl*20/100+vl))
else:
    print('Inválido!')


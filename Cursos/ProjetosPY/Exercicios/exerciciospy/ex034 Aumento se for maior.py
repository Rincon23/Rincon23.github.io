sal = float(input('Digite o salário: '))

if sal >= 1250:
    print('Novo salário após o aumento de 10%: {}'.format(sal*10/100+sal))
else:
    print('Novo salário após o aumento de 15%: {}'.format(sal*15/100+sal))
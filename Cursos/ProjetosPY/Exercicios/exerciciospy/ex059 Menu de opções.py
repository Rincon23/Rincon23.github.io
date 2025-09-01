n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
op = 5

while op != 9:

    if op == 4:
        n1 = int(input('Digite o 1º número: '))
        n2 = int(input('Digite o 2º número: '))

    print("""------Menu------
    1. Somar
    2. Multiplicar
    3. Maior
    4. Novos numeros
    9. Sair do programa""")

    if op == 1:
        print('A soma é igual a ', n1+n2)

    if op == 2:
        print('A multiplicação é igual a ', n1*n2)
    
    if op == 3:
        if n1 > n2:
            print(n1,'é maior!')
        elif n1 < n2:
            print(n2,'é maior!')
        else:
            print('Os números são iguais!')

    op = int(input('Digite a opção: '))
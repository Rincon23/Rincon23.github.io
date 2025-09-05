"""
Enunciado: Altere o programa anterior de modo que ele continue exibindo o menor dos dois valores lidos. Porém,
quando forem iguais o programa deve exibir o valor junto com o texto "Os dois números são iguais"
"""

n1 = int(input('Digite o 1º numero: '))
n2 = int(input('Digite o 2º numero: '))

if n1 < n2:
    print(f'O numero {n1} é menor')
elif n2 < n1:
    print(f'O numero {n2} é menor')
else:
    print(f'Os numeros digitados são iguais! Ambos valem {n1}')
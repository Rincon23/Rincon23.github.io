"""
Enunciado: Escreva um programa que leia dois inteiros e mostre na tela apenas o menor dos dois. Se ambos
forem iguais, mostre qualquer um deles.
"""

n1 = int(input('Digite o 1º numero: '))
n2 = int(input('Digite o 2º numero: '))

if n1 < n2:
    print(f'O numero {n1} é menor')
elif n2 < n1:
    print(f'O numero {n2} é menor')
else:
    print('Os numeros digitados são iguais!')
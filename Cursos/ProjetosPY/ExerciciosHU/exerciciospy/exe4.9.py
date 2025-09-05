"""
Enunciado: Escreva um programa que leia 3 números inteiros e mostre na tela uma das seguintes opções:
a) "Os três valores são iguais"
b) "Há dois valores iguais e um diferente"
c) "Os três valores são diferentes"
"""

n1 = int(input('Digite o 1º valor: '))
n2 = int(input('Digite o 2º valor: '))
n3 = int(input('Digite o 3º valor: '))

if n1 == n2 == n3:
    print('Os três valores são iguais')
elif n1 != n2 and n1 != n3 and n2 != n3:
    print('Os três valores são diferentes')
else:
    print('Há dois valores iguais e um diferente')


"""
Enunciado: Escreva um programa que leia um número N e em seguida exiba na tela todos os números divisíveis
por 7 entre 1 e N (inclusive)
"""

n = int(input('Digite um valor: '))
i = 1

while n+1 > i:
    if i%7 == 0:
        print(i, end=' ')
    i +=1
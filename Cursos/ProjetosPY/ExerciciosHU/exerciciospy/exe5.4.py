"""
Enunciado: Escreva um programa que leia dois números inteiros: LMin e LMax. Em seguida exiba na tela todos
os valores dentro do intervalo fechado [LMin, LMax].
"""

lmin = int(input('Digite o valor minimo '))
lmax = int(input('Digite o valor maximo '))

while lmin < lmax+1:
    print(lmin, end=' ')
    lmin+=1
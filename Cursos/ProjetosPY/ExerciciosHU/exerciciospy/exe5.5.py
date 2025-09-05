"""
Enunciado: Escreva um programa que leia três números inteiros: LMin, LMax e D. Em seguida exiba na tela todos
os valores divisíveis por D que estão dentro do intervalo fechado [LMin, LMax].
"""

lmin = int(input('Digite o valor minimo '))
lmax = int(input('Digite o valor maximo '))
d = int(input('Digite o valor que será divisível '))

while lmin < lmax+1:
    if lmin%d == 0:
        print(lmin, end=' ')
    lmin+=1
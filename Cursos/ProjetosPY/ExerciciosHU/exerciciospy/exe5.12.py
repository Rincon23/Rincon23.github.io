"""
Enunciado: Escreva um programa que leia dois inteiros: Qtde e Prim. Em seguida mostre na tela os Qtde termos
da sequência de Fibonacci que sejam maiores que Prim.
"""

n = int(input('Quantos termos de fibonacci? '))
prim = int(input('Maiores que: '))
i=0
fibo1 = 0
fibo2 = 1
resul = 0
termo1 = True

while i != n:
    if i == 0:
        if fibo1 > prim:
            print(f'{fibo1}-', end='')
            termo1 = False
    elif i == 1:
        if fibo2 > prim:
            print(f'{fibo2}', end='')
            termo1 = False
    else:
        resul = fibo1 + fibo2
        if resul > prim and termo1 == True:
            print(f'{resul}', end='')
            termo1 = False
        elif resul > prim:
            print(f'-{resul}', end='')
        fibo1 = fibo2
        fibo2 = resul
    i += 1
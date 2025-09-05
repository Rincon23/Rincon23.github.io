"""
Enunciado: Escreva um programa que leia uma quantidade Qtde e mostre na tela os Qtde primeiros termos da
sequência de Fibonacci.
A sequência de Fibonacci é definida da seguinte forma: 
a) os dois primeiros termos da sequência
são 0 e 1. Do terceiro termo em diante cada termo é a soma dos dois anteriores.
Caso de teste: Se Qtde = 9, então a sequência é: 0, 1, 1, 2, 3, 5, 8, 13, 21
"""

n = int(input('Quantos termos de fibonacci? '))
i=0
fibo1 = 0
fibo2 = 1
resul = 0

while i != n:
    if i == 0:
        print(f'{fibo1}', end='')
    elif i == 1:
        print(f'-{fibo2}', end='')
    else:
        resul = fibo1 + fibo2
        print(f'-{resul}', end='')
        fibo1 = fibo2
        fibo2 = resul
    i += 1
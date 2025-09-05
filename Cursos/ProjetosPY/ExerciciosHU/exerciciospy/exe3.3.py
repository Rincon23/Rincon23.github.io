"""
Enunciado: Escreva um programa que leia três números reais em objetos denominados A, B e C. O programa
deve calcular e mostrar na tela os resultados das fórmulas a seguir, usando 3 casas decimais.

(imagem)

"""

A = float(input('Digite 1° Numero: '))
B = float(input('Digite 2° Numero: '))
C = float(input('Digite 3° Numero: '))

R1 = A+B+C
R2 = A*B*C
R3 = 2*(A+B)-C
R4 = (A+B+C)/3
R5 = (2*B+3*C)/(5*A) 
R6 = R6 = A**2 + B**2 

print(f'R1 = {R1:.3f}\nR2 = {R2:.3f}\nR3 = {R3:.3f}\nR4 = {R4:.3f}\nR5 = {R5:.3f}\nR6 = {R6:.3f}')
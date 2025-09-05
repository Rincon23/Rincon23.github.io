"""
Enunciado: Escreva um programa que leia um número real e mostre na tela os valores de 25%, 50%, 75% do
valor lido usando o formato com 3 casas decimais mostrado abaixo:

Exemplo Valor lido: 136.7

Exibir 25% -> 34.175 - 50% -> 68.350 - 75% -> 102.525
"""

n = float(input('Digite um valor: '))

print(f'25% -> {n*25/100:.3f} - 50% -> {n*50/100:.3f} - 75% -> {n*75/100:.3f}')
"""
Enunciado: Escreva um programa que leia a idade de uma pessoa e indique qual sua classe eleitoral:
a) menor que 16 anos -> não eleitor
b) entre 18 completos e 65 anos incompletos -> eleitor obrigatório
c) entre 16 anos completos e 18 anos incompletos ou 65 anos completos -> eleitor facultativo
"""

i = int(input('Qual é a idade: '))

if i < 0:
    print('Não pode existir idade negativa!')
elif i < 16:
    print('Não eleitor')
elif i < 65:
    print('Eleitor obrigatório')
elif i >= 65:
    print('Eleitor facultativo')
    
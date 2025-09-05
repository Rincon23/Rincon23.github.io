"""
Enunciado: Nas eleições municipais os municípios com 200 mil eleitores ou mais tem segundo turno caso o
primeiro colocado não tenha mais do que 50% dos votos. Escreva um programa que leia o nome do
município, a quantidade de eleitores e a quantidade de votos do candidato mais votado e informe se
haverá segundo turno ou não
"""

nome = input('Nome do municipio: ')
qtdeleitores = int(input('Quantidade de eleitores: '))
maiorqtdvoto = int(input('Quantidade de votos do candidato mais votado: '))

if qtdeleitores >= 200000:
    if maiorqtdvoto > qtdeleitores*50/100:
        print('Não terá segundo turno')
    else:
        print('Terá segundo turno')
else:
    print('Não terá segundo turno')

"""
Enunciado: Em um determinado momento do dia a cotação de compra das moedas estrangeiras é a seguinte:
Dólar: US$ 1.00 = R$ 4.89 - Euro: € 1.00 = R$ 5.26 - Libra Esterlina: £ 1.00 = R$ 6.17
Escreva um programa que leia o tipo (D, E ou L maiúsculo) e o valor de moeda estrangeira que se
quer comprar e calcule o valor em reais necessários.
"""

Dolar = 4.89
Euro = 5.26
Libra = 6.17

vl = float(input('Quantas unidades de moeda quer comprar? '))
moeda = input('Qual moeda quer comprar? [D/E/L] ')

if moeda == 'D':
    print(f'Você poderá comprar US$ {vl} com R$ {vl*Dolar}') 
if moeda == 'E':
    print(f'Você poderá comprar € {vl} com R$ {vl*Euro}') 
if moeda == 'L':
    print(f'Você poderá comprar £ {vl} com R$ {vl*Libra}') 
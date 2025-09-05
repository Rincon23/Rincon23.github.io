"""
Enunciado: No comércio, o conceito de Margem Bruta é uma porcentagem que é aplicada ao preço de custo
para se obter o preço de venda. Uma loja tem como política comercial aplicar uma margem bruta de
45% quando o preço de custo de um produto é menor ou igual a R$ 100,00. Se o produto custa mais
que isso a margem bruta é de 35%. Escreva um programa que leia o preço de custo do produto e
mostre na tela qual o seu preço de venda, com duas casas decimais. 
"""

custo = float(input('Digite o valor do custo: '))

if custo <= 100:
    print(f'O preço de venda será de {custo*45/100+custo:.2f}')
else:
    print(f'O preço de venda será de {custo*35/100+custo:.2f}')
"""
Enunciado: Escreva um programa que permaneça em laço lendo três dados de um produto: o código (int), o
preço de compra (float) e o preço de venda(float). Com esses dados forme uma tupla e armazene-a
em uma lista. Os três dados devem ser lidos em uma única linha separados por espaço em branco.

O laço termina quando forem digitados três zeros: 0 0 0

Em seguida, para todas as tuplas presentes na lista, exiba o código do produto e a margem bruta de
lucro do produto em porcentagem e com uma casa decimal.

A margem bruta de lucro é calculada com a expressão:
𝑀𝑎𝑟𝑔𝑒𝑚𝐵𝑟𝑢𝑡𝑎 = (𝑃𝑟𝑒ç𝑜 venda/𝑃𝑟𝑒ç𝑜 de co𝑚pra*- 1 ) . 100%
"""

t = [
    ('\tcod', '\tmargem bruta')
]
linha = 0
while True:
    cod = int(input('Código do produto: '))
    compra = float(input('Preço de compra do produto: '))
    venda = float(input('Preço de venda do produto: '))

    if cod == compra == venda == 0:
        break

    cod = f'\t{cod}'
    margem = ((venda / compra) - 1) * 100

    margem = f'\t{margem:.2f}'
    l = [cod,margem]
    t.append(l)
    for i in range(len(t)):
        print()
        for j in range(len(t[i])):
            print(t[i][j], end=' ')
    print('\n')


        
        
        

    







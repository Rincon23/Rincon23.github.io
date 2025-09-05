"""
Enunciado: Escreva um programa que leia um número inteiro Qtde e carregue uma lista com essa quantidade
de números inteiros aleatórios quaisquer. Exiba a lista na tela.

Em seguida verifique se existem e elimine valores que estiverem repetidos, deixando apenas uma
ocorrência de cada. A ordem relativa dos elementos na lista não deve ser alterada, com exceção às
consequências da eliminação dos repetidos. Exiba a nova lista sem repetidos e o seu tamanho.
"""

from random import randint

qtde = int(input('Quantos numeros quer gerar? '))
l = []

for i in range(qtde):
    l.append(randint(1,30))
print(f'Lista: {l} \nTamanho da lista: {len(l)}')

for v in l:
    if l.count(v) > 1:
        for i in range(l.count(v)-1):
            l.remove(v)

print(f'Essa é a nova lista sem repetições: {l} \nTamanho da lista: {len(l)}')



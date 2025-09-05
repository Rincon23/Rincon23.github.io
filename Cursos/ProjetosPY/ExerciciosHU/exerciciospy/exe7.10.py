"""
Enunciado: Escreva um programa que leia um número inteiro Qtde e carregue uma lista com essa quantidade
de números inteiros aleatórios entre 1 e 100. Exiba a lista na tela.

Em seguida inicie um laço que deve permanecer em execução enquanto um valor inteiro X for maior
que zero. Para cada valor de X verifique se ele está na lista gerada e caso esteja elimine-o. Se houver
mais de uma ocorrência de X na lista, elimine todas. Após as eliminações exiba a lista novamente.
"""

from random import randint

qtde = int(input('Quantos numeros quer gerar? '))
l = []

for i in range(qtde):
    l.append(randint(1,100))
l.sort()
print(l)

x = 1
veri = False
while True:
    x = int(input('Digite um numero que queira retirar: '))
    if x <= 0:
        break
    if x in l:
        for i in range(l.count(x)):
            l.remove(x)
        print(f'Nova lista: {l}')
    else:
        print('O numero não está na lista!')
    

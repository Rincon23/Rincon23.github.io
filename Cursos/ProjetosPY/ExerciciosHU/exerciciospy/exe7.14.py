"""
Enunciado: Escreva um programa que leia um número inteiro nA e gere uma lista A com nA valores inteiros
aleatórios, não repetidos e situados na faixa [1, 100]. Mostre-a na tela em ordem crescente.
Em seguida leia outro inteiro nB e gere a lista B usando as mesmas regras aplicadas à lista A. Mostrea na tela também em ordem crescente.
Crie e exiba uma lista contendo a união das listas A e B, sem conter valores repetidos. Mostre a lista
resultante e a quantidade de elementos dela.

Exemplo: 
nA = 7 lista A = [8, 12, 29, 35, 44, 64, 81]
nB = 5 lista B = [10, 25, 35, 38, 64]
Saída: União de A e B
[8, 10, 12, 25, 29, 35, 38, 44, 64, 81] contém 10 elementos
"""

from random import randint

na = int(input('Quantos numeros quer gerar? '))
la = []
nb = int(input('Quantos numeros quer gerar? '))
lb = []

for i in range(na):
    la.append(randint(1,100))
for v in la:
    if la.count(v) > 1:
        for i in range(la.count(v)-1):
            la.remove(v)
            while True:
                n = randint(1,100)
                if not(n in la):
                    la.append(n)
                    break
for i in range(nb):
    lb.append(randint(1,100))
for v in lb:
    if lb.count(v) > 1:
        for i in range(lb.count(v)-1):
            lb.remove(v)
            while True:
                n = randint(1,100)
                if not(n in lb):
                    lb.append(n)
                    break
                

lb.sort()
la.sort()

print(f'nA = {na} lista A = {la}')
print(f'nb = {nb} lista B = {lb}')
la.extend(lb)

for v in la:
    if la.count(v) > 1:
        for i in range(la.count(v)-1):
            la.remove(v)

la.sort()
print(f'Saída: União de A e B\n{la} contém {len(la)} elementos')
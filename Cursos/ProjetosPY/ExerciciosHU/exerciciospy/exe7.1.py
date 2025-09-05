"""
Enunciado: Altere a solução do ex.resolvido 7.3 para exibir os números reais da lista com duas casas decimais.

ex.resolvido 7.3:
N = int(input('Digite a quantidade: '))
L = []
for i in range(N):
 X = float(input(f' elemento {i}: '))
 L.append(X)
print('\nResultado:')
for valor in L:
 print(f' {valor}')
print('Fim do Programa')
"""

N = int(input('Digite a quantidade: '))
L = []
for i in range(N):
 X = float(input(f' elemento {i}: '))
 L.append(X)
print('\nResultado:')
for valor in L:
 print(f' {valor:.2f}')
print('Fim do Programa')
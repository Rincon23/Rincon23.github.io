"""
Enunciado: Altere a solução ex.resolvido 7.3 para exibir os resultados em ordem crescente

Dica: Aplique o método .sort() apresentado no quadro 7.2 e visto no vídeo do exemplo 7.10

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
L.sort()
for valor in L:
    print(f' {valor}')
print('Fim do Programa')
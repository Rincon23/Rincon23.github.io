"""
Enunciado: Altere a solução do ex.resolvido 7.3 incluindo o comando try-except na leitura dos números reais
para evitar a digitação incorreta dos valores. Quando ocorrer uma exceção uma mensagem deve ser
exibida na tela informando esta condição.

Dica: Relembre o tratamento de exceções consultando o capítulo 6, em especial o exemplo 6.4

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
try:
    N = int(input('Digite a quantidade: '))
    L = []
    for i in range(N):
        X = float(input(f' elemento {i}: '))
        L.append(X)
        print('\nResultado:')
    for valor in L:
        print(f' {valor}')
        print('Fim do Programa')

except ValueError:
    print('Apenas utilize numeros inteiros!')
"""
Enunciado: Altere a solução ex.resolvido 7.6 de modo que todos os valores repetidos rejeitados sejam incluídos
em uma segunda lista. Ao final exiba essa segunda lista juntamente com seu tamanho.

ex.resolvido 7.6:
LstValores = []
valor = int(input('Digite um inteiro: '))
while valor != 0:
    if valor not in LstValores:
        LstValores.append(valor)
    else:
        print(f' erro! o valor {valor} já está na lista')
    valor = int(input('Digite um inteiro: '))
print('\nResultado')
print(LstValores)
print(f'A lista contém {len(LstValores)} elementos')
print('Fim do Programa')
"""

LstValores = []
LstValoresrejeitados = []
valor = int(input('Digite um inteiro: '))
while valor != 0:
    if valor not in LstValores:
        LstValores.append(valor)
    else:
        print(f' O valor {valor} já está na lista adicionamos em outra!')
        LstValoresrejeitados.append(valor)
    valor = int(input('Digite um inteiro: '))
print('\nResultado')
print(LstValores)
print(f'A lista contém {len(LstValores)} elementos\n\n')
print(LstValoresrejeitados)
print(f'A lista contém {len(LstValoresrejeitados)} elementos')
print('Fim do Programa')


"""
Enunciado: Escreva um programa que permaneça em laço lendo quantidades (números inteiros) de produtos
vendidos. O laço termina quando for digitado zero ou um valor negativo. Ao término do laço exiba na
tela a soma de todas as quantidades digitadas (se for digitado um negativo para sair do laço ele não
deve afetar o total).
"""
n = 0
soma = 0

while True:
    n = int(input('Digite um valor para a soma: '))
    if n > 0:
        soma += n
    else:
        break

print(f'A soma dos valores é: {soma}')
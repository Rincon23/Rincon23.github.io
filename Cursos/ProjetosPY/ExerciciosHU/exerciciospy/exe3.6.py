"""
Exercício Proposto 3.6
Enunciado: Uma empresa comercial trabalha com 3 vendedores externos e os remunera com R$ 1200,00 fixos
mais comissão de 6% sobre o valor total vendido no mês. Escreva um programa que leia o nome e o
total vendido pelos 3 vendedores, calcule e exiba na tela a mensagem de saída conforme o exemplo
a seguir. Exiba os valores numéricos com duas casas decimais.

Exemplo de saída:

vendedor José Carlos Santos vendeu R$ 43759.35 e faz jus a uma comissão de R$ 3825.56
vendedor Manoel Guimarães vendeu R$ 61417.81 e faz jus a uma comissão de R$ 4885.07
vendedor Plínio Pereira vendeu R$ 39336.87 e faz jus a uma comissão de R$ 3560.21

"""

n1 = input('Digite o nome do 1º Vendedor: ')
v1 = float(input('Digite valor que o 1º Vendedor vendeu: '))

n2 = input('Digite o nome do 2º Vendedor: ')
v2 = float(input('Digite valor que o 2º Vendedor vendeu: '))

n3 = input('Digite o nome do 3º Vendedor: ')
v3 = float(input('Digite valor que o 3º Vendedor vendeu: '))

print(f"""
vendedor {n1} vendeu R$ {v1:.2f} e faz jus a uma comissão de R$ {v1*6/100+1200:.2f}
vendedor {n1} vendeu R$ {v2:.2f} e faz jus a uma comissão de R$ {v2*6/100+1200:.2f}
vendedor {n1} vendeu R$ {v3:.2f} e faz jus a uma comissão de R$ {v3*6/100+1200:.2f}
""")
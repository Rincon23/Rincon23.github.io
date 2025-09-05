"""
Enunciado: Escreva um programa que leia um número inteiro e informe se esse número é primo ou não.
Lembrando: um número primo é divisível apenas por 1 e por ele mesmo.
"""

n = int(input('Digite o número para verificar se ele é ou não um número primo: '))
primo = True

for i in range(2,n-1):
    if n%i==0:
        primo = False

if primo == False:
    print('Ele não é um numero primo!')
else:
    print('Ele é um numero primo!')
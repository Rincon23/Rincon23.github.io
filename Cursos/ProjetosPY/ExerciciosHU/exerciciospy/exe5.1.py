"""
Enunciado: Reescreva o Exercício Resolvido 5.5 de modo a eliminar o comando if que foi acrescentado dentro
do laço while. Procure pensar em uma forma de eliminar esse condicional e ao mesmo tempo
manter o programa correto, totalizando e contando os valores diferentes de zero que forem
digitados.

Dica: a solução consiste em alterar a ordem dos comandos existentes dentro do laço while.

Exercício Resolvido 5.5:

d = int(input('Digite um valor maior que 0 :'))

if d<=0:
    print(f'O valor {d} é inválido')
else:
    i = 1
    while i < 100:
        if i % d == 0:
            print(i)
        i +=1

"""

d = int(input('Digite um valor maior que 0 :'))

if d<=0:
    print(f'O valor {d} é inválido')
else:
    i = d
    while i < 100:
        print(i)
        i += d








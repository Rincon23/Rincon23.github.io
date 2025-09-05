from random import choice

al1 = input('Nome do aluno 1: ')
al2 = input('Nome do aluno 2: ')
al3 = input('Nome do aluno 3: ')
al4 = input('Nome do aluno 4: ')

escolhido = choice([al1, al2, al3, al4])
print('O escolhido foi', escolhido)
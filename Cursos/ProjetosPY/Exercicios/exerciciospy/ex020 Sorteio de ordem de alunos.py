from random import sample

al1 = input('Nome do aluno 1: ')
al2 = input('Nome do aluno 2: ')
al3 = input('Nome do aluno 3: ')
al4 = input('Nome do aluno 4: ')

ordem = sample([al1, al2, al3, al4], k=4)

print('A ordem de apresentação é:', ordem)
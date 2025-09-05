"""
Enunciado: Leia um número inteiro entre 1 e 12 e exiba o mês correspondente. Caso seja digitado um número
fora desse intervalo, o programa deve exibir uma mensagem informando que não existe mês com
este número.
"""

n = int(input('Digite o numeor do mês: '))

if n == 1:
    print('Janeiro')
elif n == 2:
    print('Fevereiro')
elif n == 3:
    print('Março')
elif n == 4:
    print('Abril')
elif n == 5:
    print('Maio')
elif n == 6:
    print('Junho')
elif n == 7:
    print('Julho')
elif n == 8:
    print('Agosto')
elif n == 9:
    print('Setembro')
elif n == 10:
    print('Outubro')
elif n == 11:
    print('Novembro')
elif n == 12:
    print('Dezembro')
else: 
    print('Não existe mês com este número')
"""
Enunciado: Escreva um programa para exibir na tela o nome e a categoria de um lutador. O programa deve ler
um string para o nome e um número real para o peso. Conforme o peso ocorrerá o enquadramento
na categoria, segundo esta tabela (fictícia):

(Imagem)
"""

nome = input('Qual é o nome do lutador? ')
peso = float(input('Qual é o peso do lutador? '))
cat = ''

if peso < 0:
    cat = ''
elif peso < 52:
    cat = 'invalido'
elif peso < 65:
    cat = 'Pena'
elif peso < 72:
    cat = 'Leve'
elif peso < 79:
    cat = 'Ligeiro'
elif peso < 86:
    cat = 'Meio-Médio'
elif peso < 90:
    cat = 'Médio'
elif peso < 100:
    cat = 'Meio-Pesado'
elif peso >=100:
    cat = 'Pesado'    

if cat != '':
    print(f'O lutador {nome} está na categoria {cat}')
else:
    print('Não pode valor negativo!')
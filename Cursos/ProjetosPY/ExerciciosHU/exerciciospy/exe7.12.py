"""
Enunciado: Escreva um programa que permaneça em laço de modo que em cada repetição seja lido e
armazenado em uma lista o nome de uma pessoa. O laço termina quando o usuário entrar com um
string vazio.
Exiba na tela a lista de nomes em ordem alfabética e precedida de um número de ordem começando
em 1.
Exemplo: 1 Bernardo Almeida
2 Carlos Eduardo Soares
3 Julia Monteiro da Silva
4 Margarete Guimarães
5 Robson de Souza Andrade
"""
nome = '-'
l = []

while True:
    nome = input('Digite o nome ou não digite nada para parar: ')
    
    if nome == '':
        break
    
    l.append(nome)

l.sort()

for i in range(len(l)):
    print(f'{i+1}. {l[i]}')
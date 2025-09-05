"""
Enunciado: Escreva um programa que permaneça em laço lendo cadeias de caracteres (strings). Para cada
cadeia digitada o programa deve exibir a cadeia seguida da quantidade de caracteres que ela
contém. O programa termina quando for digitado "FIM" (em letras maiúsculas).
"""

cad = ''

while cad != 'FIM':
    cad = input('Digite uma cadeia de caracteres ou "FIM" para parar: ')
    if cad != 'FIM':
        print(f'A cadeia "{cad}" tem {len(cad)} letras')
print(cad)
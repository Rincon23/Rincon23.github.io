frase = str(input('Digite uma frase: ').lower())

print('Aparece a letra A {} veses'.format(frase.count('a')))
print('A primeira vez que a letra "a" foi encontrada foi na posição {}'.format(frase.find('a')))
print('A ultima vez que a letra "a" foi encontrada foi na posição {}'.format(frase.rfind('a')))
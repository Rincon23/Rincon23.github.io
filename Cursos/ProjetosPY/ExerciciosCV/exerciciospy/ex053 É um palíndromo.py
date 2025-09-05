frase = input('Digite uma frase: ')
frase = ''.join(frase.split())
#frase = frase.replace(' ','')
frase2=''

for i in range(len(frase)-1,-1,-1):
    frase2 += frase[i]

if frase != frase2:
    print('A frase não é um palindromo!')
else:
    print('A frase é um palindromo!')



op = ''
n = 0
soma = 0
c = 0
maior = 0
menor = 0
while op != 'n':

    n = int(input('Digite um numero: '))
    soma += n
    c +=1

    if c == 1:
        maior = n
        menor = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n

    op = ''
    while op != 's' and op != 'n':
        op = input('Quer continuar? [s/n] ')

print("""------------
Média dos valores: {}
Maior valor: {}
Menor valor: {}
""".format(soma/c,maior,menor))
n = 0
soma = 0
c = 0
while n != 999:

    n = int(input('Digite o numero para somar ou 999 para parar: '))
    if n != 999:
        soma += n
        c +=1

print("""------------
A soma dos numeros: {}
Contagem dos numeros: {}
""".format(soma,c))
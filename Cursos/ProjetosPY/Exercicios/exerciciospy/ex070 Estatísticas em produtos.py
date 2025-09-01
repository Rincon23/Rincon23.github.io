tot = 0
cont1000 = 0
nomemaiscaro = ''
maiscaro = 0
continuar = ''

while True:

    nome = input('Nome do produto: ')
    preco = int(input('Qual é preço do produto: '))
    
    tot += preco

    if preco > 1000:
        cont1000 +=1

    if preco > maiscaro:
        maiscaro = preco
        nomemaiscaro = nome

    while continuar != 's' and continuar != 'n': 
        continuar = input('Quer continuar? [s/n] ')

    if continuar == 'n':
        break
    
    continuar = ''
    


print(f"""---------------
Total gasto: {tot}
Quantos custam acima de R$1000: {cont1000}
Nome do produto mais caro: {nomemaiscaro} que custou {maiscaro}""")
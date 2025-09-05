contmaioridade = 0
contm = 0
contf20 = 0
continuar = ''
while True:
    idade = int(input('Qual é a idade: '))
    sex = input('Masculino ou feminino? [m/f]')

    if idade > 18:
        contmaioridade +=1

    if sex == 'm':
        contm +=1

    if sex == 'f' and idade < 20:
        contf20 += 1

    while continuar != 's' and continuar != 'n': 
        continuar = input('Quer continuar? [s/n] ')

    if continuar == 'n':
        break
    
    continuar = ''


print(f'---------------\nQuantas pessoas tem mais de 18 anos: {contmaioridade}\nQuantos homens: {contm}\nQuantas mulheres com menos de 20 anos: {contf20}')
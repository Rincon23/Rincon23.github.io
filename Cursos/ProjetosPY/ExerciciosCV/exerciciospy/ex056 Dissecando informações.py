somaidade = 0
idadevelho = -1
nomevelho = 'Não existem homens'
mulhermenorde20 = 0
for i in range(1,5):
    print('{}ª Pessoa'.format(i))
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo [m/f]: ')

    somaidade += idade

    #Homem mais velho
    if sexo == 'm' and idadevelho > idade:
        idadevelho = idade
        nomevelho = nome

    #Quantas mulheres tem menos de 20 anos
    if sexo == 'f' and idade < 20:
        mulhermenorde20 += 1



print("""Média da idade: {}
Nome do homem mais velho: {}
Quantas mulheres tem menos de 20 anos: {}""".format(somaidade/4, nomevelho, mulhermenorde20))
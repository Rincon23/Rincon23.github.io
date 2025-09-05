idade = int(input('Quantos anos você tem? '))

if idade == 18:
    print('Está na hora de se alisatar!')
elif idade < 18:
    print('Não está na hora ainda de se alistar')
    print('Ainda restam {} anos'.format(18-idade))
elif idade > 18:
    print('Espero que você já tenha se alistado!')
    print('Se não se alistou já está {} anos atrasado'.format(idade-18))
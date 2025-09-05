i = int(input('Digite a idade: '))

if i<0:
    print('Idade inválida')
elif i <= 9:
    print('Categoria: Mirim')
elif i <= 14:
    print('Categoria: Infantil')
elif i <= 19:
    print('Categoria: Junior')
elif i <= 20:
    print('Categoria: Sênior')
else:
    print('Categoria: Master')
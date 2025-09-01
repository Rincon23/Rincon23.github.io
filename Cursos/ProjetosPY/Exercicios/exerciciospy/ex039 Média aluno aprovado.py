n1 = float(input('Digite a 1° nota: '))
n2 = float(input('Digite a 2° nota: '))
m = (n1+n2)/2

print('A media foi {}'.format(m))

if m>=7:
    print('Aprovado!')
elif m>=5 and m<6.9:
    print('Recuperação!')
elif m<5:
    print('Reprovado!')
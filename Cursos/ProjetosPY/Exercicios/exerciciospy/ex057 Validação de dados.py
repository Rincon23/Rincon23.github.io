sex = ''

while sex != 'M' and sex != 'F':
    sex = input('Qual é o sexo? ')
    if sex != 'M' and sex != 'F':
        print('Digite certo! Apenas F ou M')
print('OK!')
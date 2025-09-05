"""
Enunciado: Altere o programa do Exercício Proposto 7.8 acrescentando uma validação adicional para garantir
que a data fornecida seja válida. Por exemplo: a entrada 20242255 é válida segundo os critérios
estabelecidos no enunciado 7.8. Porém, 55/22/2024 não é uma data válida.

Neste exercício você deve garantir que a data seja válida (incluindo anos bissextos - para identificar
se um ano é bissexto veja o Exercício Proposto 4.8).

enunciado 7.8: 
data = int(input('Digite uma data no formato aaaammdd: '))
data = str(data) 

if len(data) == 8:
    print(f'A data fornecida foi: {data[len(data)-2:]}/{data[4:6]}/{data[:4]}')

Exercício Proposto 4.8:
ano = int(input('Digite um ano: '))

if ano%4 == 0 and not(ano%100 == 0) or ano%400 == 0:
    print('É um ano Bissexto')
else:
    print('Não é um ano Bissexto')

"""

data = input('Digite uma data no formato aaaammdd: ')
Bissexto = False
mes31 = ['01','03','05','07','08','10','12']


try:
    int(data)
    dia = data[len(data)-2:]
    mes = data[4:6]
    ano = data[:4]
    fevereiro = True


    if int(ano)%4 == 0 and not int(ano)%100 == 0 or int(ano)%400 == 0:
        Bissexto = True

    if mes == '02':
        if dia == '29' and Bissexto == False:
            fevereiro = False
        elif dia in ['30','31']:
            fevereiro = False
    

    if len(data) == 8:
        if int(dia) > 0 and int(dia) < 32:
            if int(mes) > 0 and int(mes) < 13:
                if dia == '31' and mes in mes31 or dia != '31':
                    if mes != '02' or fevereiro == True:
                        print(f'A data fornecida foi: {dia}/{mes}/{ano}')
                    else:
                        print('fevereiro tem apenas 28 dias e 29 no ano bissexto!')
                else:
                    print(f'O mes {mes} não tem {dia} dias')
            else:
                print('O mes só pode ser entre 1 e 12 meses!') 
        else:
            print('O dia só pode ser de 1 a 31!')

    else:
        print('Data com formato inválido!')   

except ValueError:
    print('Data não compreendida')

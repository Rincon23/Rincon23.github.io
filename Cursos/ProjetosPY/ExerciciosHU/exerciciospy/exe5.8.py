"""
Enunciado: Uma indústria metalúrgica adota um código de produto com o seguinte formato TMMM, onde T indica
o uso do produto, sendo 1 para residencial; 2 para industrial e MMM indica qual é o produto.
Escreva um programa que permaneça em laço até que seja digitado 0. Em cada repetição leia duas
informações:
a) O código do produto;
b) A quantidade vendida desse produto
O programa deve totalizar separadamente e exibir na tela as quantidades de produtos residenciais e
industriais vendidos. Se o dígito T do código não for 1 ou 2 deve ser mostrado "Tipo Inválido" e a
quantidade deve ser ignorada.
"""
i = -1
cod = 1
t1 = 0
t2 = 0
while cod != 0:
    while True:
        codj = input('Digite o codigo do produto: ')
        cod = int(codj[0])
        if cod != 0:
            qtd = int(codj[1:4])
        if cod in [0,1,2]:
            if cod == 1:
                t1 += qtd
            if cod == 2:
                t2 += qtd
            break
        else:
            print('Tipo Inválido ')

print(f'Foram vendidos {t1} residenciais\nForam vendidos {t2} industriais')
    
    
    

"""
Enunciado: Escreva um programa para uma fábrica de calçados que leia o código LL de um calçado, que é um
número inteiro com 2 dígitos. Exiba na tela a linha do calçado, conforme a tabela a seguir. Se o
número fornecido não estiver na tabela, deve-se exibir a mensagem "Código inválido".

LL Linha de calçados    LL  Linha de calçados
16 Bebê                 49  Masculino esportivo
23 Infantil feminino    52  Feminino formal salto baixo
25 Infantil masculino   53  Feminino formal salto alto
29 Infantil esportivo   55  Feminino casual salto baixo
42 Masculino formal     56  Feminino casual salto alto
43 Masculino casual     59  Feminino esportivo

"""

cod = int(input('Digite o código: '))

if cod == 16:
    print('Bebê')
elif cod == 23:
    print('Infantil feminino')
elif cod == 25:
    print('Infantil masculino')
elif cod == 29:
    print('Infantil esportivo')
elif cod == 42:
    print('Masculino formal')
elif cod == 43:
    print('Masculino casual')
elif cod == 49:
    print('Masculino esportivo')
elif cod == 52:
    print('Feminino formal salto baixo')
elif cod == 53:
    print('Feminino formal salto alto')
elif cod == 55:
    print('Feminino casual salto baixo')
elif cod == 56:
    print('Feminino casual salto alto')
elif cod == 59:
    print('Feminino esportivo')
else:
    print('Código inválido')

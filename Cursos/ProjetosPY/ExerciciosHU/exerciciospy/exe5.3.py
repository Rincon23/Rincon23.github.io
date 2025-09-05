"""
Enunciado: Escreva um programa que obrigatoriamente leia um inteiro que esteja no intervalo fechado
[100, 200]. Se o valor fornecido estiver fora do intervalo o programa deve avisar que o valor é inválido
e permanecer no laço. Quando um valor válido for fornecido o programa deve informar que o valor
foi aceito e terminar.
"""
n = 0

while True:
    n = int(input('Digite um valor entre 100 e 200: '))
    if n < 100 or n > 200:
        print('Digite um valor válido!')
    else:
        print('Fim do programa!')
        break

    

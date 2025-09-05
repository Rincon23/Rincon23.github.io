n = int(input('Digite um numero inteiro: '))
op = int(input("""
1 para converter para Binário.
2 para converter para Octal.
3 para converter para Hexadecimal.
Digite: """))

if op == 1:
    print('O numero {} convertido para Binário é {}'.format(n, bin(n)[2:]))
elif op == 2:
    print('O numero {} convertido para Octal é {}'.format(n, oct(n)[2:]))
elif op == 3:
    print('O numero {} convertido para Hexadecimal é {}'.format(n, hex(n)[2:].upper()))
else:
    print('Digite um numero válido!')

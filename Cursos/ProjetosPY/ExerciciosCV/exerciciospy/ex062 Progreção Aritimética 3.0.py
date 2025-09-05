pt = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
i = 10

op = 0

while i != 0:
    print(pt)
    pt += r
    i-=1


while op != 9:
    print("""------Menu------
    1. Quero mais termos!
    9. Sair
    """)
    op = int(input('Digite a opção: '))

    if op == 1:
        amais = int(input('Mais Quantos termos? '))
        print('Aqui estão mais {} termos:'.format(amais))
        while amais != 0:
            print(pt)
            pt += r
            amais -=1
    

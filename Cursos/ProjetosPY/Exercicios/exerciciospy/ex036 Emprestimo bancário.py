vlcasa = float(input('Qual é o valor da casa? '))
sal = float(input('Qual é o seu salário? '))
anos = int(input('Quantos anos pretende pagar? '))

if vlcasa/anos <= 30*sal/100:
    print("""Empréstimo aprovado!
Você terá que pagar: R${:.2f} por mes durante {} anos""".format(vlcasa/anos,anos))

else:
    print("""Empréstimo desaprovado!
Você comprometeria seu salário em mais de 30% caso aprovado!
Você teria que pagar: R${:.2f} por mes durante {} anos""".format(vlcasa/anos,anos))
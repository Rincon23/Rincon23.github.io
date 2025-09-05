n = int(input('Numero: '))+10000
n = str(n)

print("""Manipulando string:
Milhar: {}
Centena: {}
Dezena: {}
Unidade: {}""".format(n[1],n[2],n[3],n[4]))

n = int(n)-10000

nmilhar = n//1000
ncentena = n//100 - (nmilhar*10)
ndezena = (n - (nmilhar*1000) - (ncentena*100))//10
nunidade = (n - (nmilhar*1000) - (ncentena*100) - (ndezena*10))



print("""\nManipulando int:
Milhar: {}
Centena: {}
Dezena: {}
Unidade: {}""".format(nmilhar, ncentena, ndezena, nunidade))


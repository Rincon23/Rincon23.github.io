mai = 0
men = 0

for i in range(0,7):
    idade = int(input('Quantos anos: '))
    if idade >= 18:
        mai += 1
    else:
        men += 1

print("""Contagem:
{} pessoas são de maioridade
{} são de menoridade""".format(mai,men))
pmo=0
pma=0


for i in range(0,5):
    p = float(input('Digite o peso: '))
    if i == 0:
        pma = p
        pmo = p
    if p > pma:
        pma = p
    if p < pmo:
        pmo = p

print('Peso maior: {} \nPeso Menor: {}'.format(pma,pmo))
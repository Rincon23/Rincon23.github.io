h = float(input('Qual é a altura da parede? '))
w = float(input('Qual é a largura da parede? '))

print('Sabendo que cada litro de tinta pinta uma área de 2m² então:')
print('Com uma parede de {}m² você irá utilizar {} litros de tinta'.format(h*w,h*w/2))
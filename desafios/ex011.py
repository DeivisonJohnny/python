largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))

area = largura * altura

print('Sua parede tem a dimensão de {}x{} e sua área é de {}m2'.format(largura, altura, area))

tinta = area / 2

print('Para pintar essa parede você vai precisar de {}L de tinta'.format(tinta))
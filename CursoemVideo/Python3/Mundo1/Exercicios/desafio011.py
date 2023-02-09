largura = float(input('Quantos metros de largura tem sua parede? '))
altura = float(input('Qantos metros de altura tem sua parede? '))
area = largura * altura
tinta = area / 2
print('Sua parede tem dimensão de {}x{} e {}m² de área.'.format(largura, altura, area))
print('Você precisa de {}L de tinta para pintar essa parede.'.format(tinta))

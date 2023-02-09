km = float(input('Qual a distância da sua viagem em Km ? '))
print('Sua viagem é de {}Km.'.format(km))
# if km <= 200:
#    valor = km * 0.50
# else:
#    valor = km * 0.45
valor = km * 0.50 if km <= 200 else km * 0.45
print('Sua passagem custará R${:.2f}! Boa viajem!'.format(valor))


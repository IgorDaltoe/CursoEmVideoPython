velo = float(input('Qual é a velocidade do carro em Km/h ? '))
multa = (velo-80) * 7
print('O limite de velocidade é 80Km/h.')
if velo > 80:
    print('O seu carro está a {}Km/h e ultrapassou o limite de velocidade!'.format(velo))
    print('Você será multado em R${:.2f}!'.format(multa))
else:
    print('O seu carro está a {:.0f}Km/h, Boa Viagem!'.format(velo))

real = float(input('Quantos Reais você tem na carteira? R$'))
dolar = real / 5.2914
euro = real * 0.1825
print('Você pode comprar US${:.2f}'.format(dolar))
print('Você pode comprar £${:.2f}'.format(euro))



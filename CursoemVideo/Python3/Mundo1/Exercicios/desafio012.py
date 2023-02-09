n1 = float(input('Qual o preço do produto ? R$'))
desc = n1 - (n1 * 5/100)
print('Na liquidação esse produto tem 5% de desconto e sai por {:.2f}R$!'.format(desc))

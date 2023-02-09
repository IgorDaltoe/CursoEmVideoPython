preco = float(input("Por favor indique o preço do produto: R$"))
print(""""Por favor escolha a forma de pagamento da lista abaixo:
[1] para Pagamento à vista no dinheiro/cheque com 10% de desconto.
[2] para à vista no cartão com 5% de desconto.
[3] para comprar no cartão em até 2x sem juros.
[4] para comprar no cartão com parcelas acima de 3x com justos de 20%""")
pagamento = int(input("Qual a sua opção: "))
pagar = float(0)
if pagamento == 1:
    pagar = preco - (preco * 10 / 100)
    print("""Sua compra será à vista no dinheiro/cheque com 10% de desconto.
Sua compra de R${:.2f} vai custar R${:.2f}""".format(preco, pagar))
elif pagamento == 2:
    pagar = preco - (preco * 5 / 100)
    print("""Sua compra será à vista no cartão com 5% de desconto.
Sua compra de R${:.2f} vai custar R${:.2f}""".format(preco, pagar))
elif pagamento == 3:
    pagar = preco / 2
    print("""Sua compra será parcelada em 2x no cartão sem juros.
Sua compra de R${:.2f} será pago em 2 parcelas de R${:.2f}""".format(preco, pagar))
elif pagamento == 4:
    parcelas = int(input("Em quantas vezes deseja parcelar ? "))
    pagar = (preco + (preco * 20 / 100)) / parcelas
    print("""Sua compra será parcelada em {0}x no cartão com juros de 20%.
Sua compra de R${1:.2f} vai custar R${2:.2f} e será pago em {0} parcelas de R${3:.2f}""".format(parcelas, preco, preco * 1.20 , pagar))
else:
    print("OPÇÃO DE PAGAMENTO INVALIDA. Tente novamente.")

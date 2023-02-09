print("-*"*25)
titulo = str("LISTA DE COMPRAS")
final = str("FIM DO PROGRAMA")
print(f"{titulo:^50}")
print("-"*50)
total = maisDeMil = preçoBarato = nomeBarato = 0
while True:
    nome = str(input("Nome do produto: ")).title()
    preço = float(input("Preço do produto: R$"))
    print("-"*50)
    if preçoBarato == 0 or preço < preçoBarato:
        preçoBarato = preço
        nomeBarato = nome
    # if preço < preçoBarato:
    #     preçoBarato = preço
    #     nomeBarato = nome
    if preço > 1000:
        maisDeMil += 1
    total += preço
    conti = " "
    while conti not in "SN":
        conti = str(input("Quer adicionar mais produtos ? [S/N] ")).strip().upper()[0]
    print("-"*50)
    if conti in "N":
        break
print(f"Total a pagar: R${total:.2f}")
print(f"{maisDeMil} produtos custam mais de R$1000.00")
print(f"O produto mais barato é o {nomeBarato} que custa R${preçoBarato:.2f}")
print("-"*50)
print(f"{final:^50}")
print("-*"*25)

pessoas = ["Maria", "Joaquina", "Debora", "Marilia", "Margarete"]
pesos = []
for c in range (0, 5):
    quilos = float(input("Quatos quilos pesa {} ? ".format(pessoas[c])))
    pesos.append(quilos)
pesos.sort()
print("O maior peso foi {} e o menor peso foi {}".format(pesos[4], pesos[0]))

# Solução do professor
# maior = 0
# menor = 0
# for p in range (1, 6):
#     peso = float(input("Digite o peso da {}ª pessoa: ".format(p)))
#     if p == 1:
#         maior = peso
#         menor = peso
#     else:
#         if peso > maior:
#             maior = peso
#         if peso < menor:
#             menor = peso
# print("O maior peso lido foi de {}Kg \nO menor peso lido foi de {}kg".format(maior, menor))
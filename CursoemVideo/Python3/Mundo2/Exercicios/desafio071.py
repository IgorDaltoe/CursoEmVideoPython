cedula1 = cedula10 = cedula20 = cedula50 = 0
titulo = ("BEM VINDO AO BANCO PYTHON")
final = ("Volte sempre ao BANCO DO PYTHON")
print("="*35)
print(f"{titulo:^35}")
print("="*35)
saque = int(input("Quanto deseja sacar ? R$"))
cedula50 = int(saque / 50)
if saque % 50 != 0:
    cedula20 = int((saque % 50) / 20)
    if (saque % 50) % 20 != 0:
        cedula10 = int(((saque % 50) % 20) / 10)
        if ((saque % 50) % 20) % 10 != 0:
            cedula1 = int((((saque % 50) % 20) % 10) / 1)
print("-"*35)
if cedula50 > 0:
    print(f"Total de {cedula50} cedulas de R$50.00")
if cedula20 > 0:
    print(f"Total de {cedula20} cedulas de R$20.00")
if cedula10 > 0:
    print(f"Total de {cedula10} cedulas de R$10.00")
if cedula1 > 0:
    print(f"Total de {cedula1} cedulas de R$1.00")
print("="*35)
print(f"{final:^35}")
print("="*35)

# resolução do professor
# print("="*30)
# valor = int(input("Que valor vc quer sacar ? R$"))
# total = valor
# céd = 50
# totcéd = 0
# while True:
#     if total >= céd:
#         total -= céd
#         totcéd += 1
#     else:
#         if totcéd > 0:
#             print(f"Total de {totcéd} cédulas de R${céd}")
#         if céd == 50:
#             céd = 20
#         elif céd == 20:
#             céd = 10
#         elif céd == 10:
#             céd = 1
#         totcéd = 0
#         if total == 0:
#             break
# print("="*30)

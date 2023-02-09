maiorDe18 = homens = mulherMenos20 = 0
titulo = str("PROGRAMA DE CADASTRO")
texto1 = str("CADASTRE UMA PESSOA")
final = str("FIM DO PROGRAMA")
print("="*45)
print(f"{titulo:^45}")
print("-"*45)
while True:
    print(f"{texto1:^45}")
    print("-"*45)
    idade = int(input("Digite a idade da pessoa: "))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Digite o sexo da pessoa [M/F]: ")).strip().upper()[0]
    print("-"*45)
    print("Cadastro concluido.")
    if idade > 18:
        maiorDe18 += 1
    if sexo in "M":
        homens += 1
    if sexo in "F" and idade < 20:
        mulherMenos20 += 1
    continuar = " "
    while continuar not in "SN":
        continuar = str(input("Deseja cadastrar mais uma pessoa ? [S/N] ")).strip().upper()[0]
    print("-"*45)
    if continuar == "N":
        break
print(f"""Dentre todos as pessoas cadastradas:
{maiorDe18} pessoas são maiores de 18 anos.
{homens} são homens.
{mulherMenos20} são mulheres menores de 20 anos.""")
print("-"*45)
print(f"{final:^45}")
print("="*45)

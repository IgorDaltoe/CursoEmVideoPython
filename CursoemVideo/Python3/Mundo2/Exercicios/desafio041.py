import datetime
anoAtual = datetime.date.today().year
print("Confederação Nacional de Natação")
anoNascimento = int(input("Digite o ano em que o atleta nasceu: "))
idade = anoAtual - anoNascimento
print("O atleta tem {} anos".format(idade))
if idade <= 9:
    print("Classificação: MIRIM")
elif idade <= 14:
    print("Classificação: INFANTIL")
elif idade <= 19:
    print("Classificação: JUNIOR")
elif idade <= 25:
    print("Classificação: SÊNIOR")
else:
    print("Classificação: MASTER")
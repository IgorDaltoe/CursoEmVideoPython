n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
media = (n1 + n2) / 2
print("A média do aluno é {:.1f}".format(media))
if media < 5:
    print("O aluno está REPROVADO!")
# elif 7 > media >= 5:
elif media >= 5 and media < 6.9:
    print("O aluno está de RECUPERAÇÃO!")
else:
    print("O aluno está APROVADO!")

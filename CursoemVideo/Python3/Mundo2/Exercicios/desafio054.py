import datetime
anoAtual = datetime.date.today().year
adulto = 0
menor = 0
pessoas = ["João", "Maria", "Pedro", "Ana", "José", "Bruna", "Gabriel"]
for c in range (0, 7):  
    anoNascimento = int(input("Em qual ano nasceu {} ? ".format(pessoas[c])))
    pessoas[c] = anoNascimento
    if anoAtual - pessoas[c]  >= 21:
        adulto += 1
    else:
        menor += 1
print("Dessas 7 pessoas {} ainda não atingiram a maioridade e {} já atingiram a mioridade.".format(menor, adulto))

print("Financie sua casa aqui mesmo!\nAntes de fazer o empréstimo primeiro me diga os seguintes dados:")
casa = float(input("Qual é o valor da casa ? R$"))
salario = float(input("Qual é o seu salário mensal ? R$"))
anos = float(input("Em quantos anos pretende pagar o empréstimo ? "))
anos = anos * 12
prestacao = casa / anos
limite = salario * 0.30
if prestacao >= limite:
    print("\033[31mLIMITE EXCEDIDO\033[m\nVocê não pode pegar esse empréstimo por que as prestações excedem 30% do seu salário!")
else:
    print("\033[32mParabéns\033[m\nEmpréstimo feito com sucesso! você irá pagar {:.0f} prestações de R${:.2f} por mês!".format(anos, prestacao))

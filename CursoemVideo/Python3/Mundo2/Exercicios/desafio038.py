n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))

cores = {"limpa": "\033[m",
        "amarelo": "\033[33m",
        "azul": "\033[34m"}

if n1 > n2: 
    print("O {0}primeiro valor{1} é {2}maior.{1}".format(cores["amarelo"], cores["limpa"], cores["azul"]))
elif n2 > n1:
    print("O {0}segundo valor{1} é {2}maior.{1}".format(cores["amarelo"], cores["limpa"], cores["azul"]))
elif n1 == n2:
    print("{0}Não existe{1} valor maior, os dois são {2}iguais.{1}".format(cores["amarelo"], cores["limpa"], cores["azul"]))
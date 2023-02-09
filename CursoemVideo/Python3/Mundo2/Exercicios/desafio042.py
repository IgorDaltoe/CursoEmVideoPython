print("Vamos tentar formar um triângulo e descobrir seu tipo!")
n1 = float(input("Digite o comprimentos de uma semirreta: "))
n2 = float(input("Digite o comprimenro de outra semirreta: "))
n3 = float(input("Digite o comprimento de mais uma semirreta: "))
retas = [n1, n2, n3]
retas.sort()
menor = retas[0] + retas[1]
triangulo = bool(menor > retas[2])
if triangulo == True:
    if n1 == n2 == n3:
        trianguloTipo = "EQUILÁTERO"
    elif n1 != n2 != n3 != n1:
        trianguloTipo = "ESCALENO"
    elif triangulo == True:
        trianguloTipo = "ISÓSCELES"
    print("Essas semirretas CONSEGUEM FORMAR um triângulo {}!".format(trianguloTipo))
else:
    print("Essas semirretas NÃO CONSEGUEM FORMAR um triângulo!")

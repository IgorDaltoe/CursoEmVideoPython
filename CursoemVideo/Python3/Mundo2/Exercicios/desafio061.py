primeiroTermo = int(input("Digite o primeiro termo da PA: "))
razão = int(input("Digite a razão da PA: "))
contador = 0
while contador < 10:
    print(primeiroTermo, end=" ")
    primeiroTermo += razão
    contador += 1

primeiroTermo = int(input("Digite o primeiro termo da PA: "))
razão = int(input("Digite a razão da PA: "))
contador = 0
termos = 10
if termos != contador:
    while contador < termos:
        print(primeiroTermo, end=" ")
        primeiroTermo += razão
        contador += 1
        if contador == termos:
            termos = int(input("\nDeseja mostrar mais quantos termos ? "))
            termos += contador
print("Progressão finalizada com {} termos mostrados".format(termos))
print("O programa será encerrado")

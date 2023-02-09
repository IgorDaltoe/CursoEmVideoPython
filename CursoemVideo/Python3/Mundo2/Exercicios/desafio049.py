n = int(input("Digite um número para ver sua tabuada: "))
print("Tabuada de {}:".format(n))
for c in range(1, 11):
    print("{} x {:2} = {}".format(n, c, n * c))

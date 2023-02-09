n = int(input("Digite um valor para descobrir seu fatorial: "))
resultado = n
for c in range(n-1, 0, -1):
    resultado *= c
# print("O fatorial de {} é = {}".format(n, resultado))
print(f"O fatorial de {n} é = {resultado}")

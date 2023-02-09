print("Sequência de Fibonacci")
n = int(input("Até qual termo deseja mostrar ? "))
penultimo = 0
ultimo = 1
# contador = 2
fibonacci = [penultimo, ultimo]
if n == 0:
    print("Erro! O programa será encerrado.")
elif n == 1:
    print(fibonacci[0])
elif n == 2:
    print(fibonacci)
else:
    for c in range (3, n+1):
        ultimo = ultimo + penultimo
        penultimo = ultimo - penultimo
        fibonacci.append(ultimo)
        # contador += 1
    print(fibonacci)

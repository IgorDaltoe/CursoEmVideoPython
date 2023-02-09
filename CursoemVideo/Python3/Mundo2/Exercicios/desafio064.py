n = qnt = soma = 0
n = int(input("Digite um valor [Digite 999 para terminar o programa]: "))
while n != 999:
    soma += n
    qnt += 1
    n = int(input("Digite um valor [Digite 999 para terminar o programa]: "))
print("Você digitou {} números\nA soma entre os números digitados é : {}".format(qnt, soma))
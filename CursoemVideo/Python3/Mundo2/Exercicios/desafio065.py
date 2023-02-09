# Resolução do professor
resp = "S"
soma = qnt = média = maior = menor = 0
while resp in "S":
    núm = int(input("Digite um número: "))
    soma += núm
    qnt += 1
    if qnt == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm
    resp = str(input("Quer continuar ? [S/N] ")).strip().upper()[0]
média = soma / qnt
print("Você digitou {} números e a média foi {}".format(qnt, média))
print("O maior valor foi {} e o menor foi {}".format(maior, menor))

# Minha resolução
# n = int(input("Digite um número: "))
# maior = n
# menor = n
# count = 1
# mediacalc = n
# continuar = str(input("Deseja continuar:[S/N] ")).strip().upper()[0]
# while continuar not in "SN":
#     print("Opção inexistente.")
#     continuar = str(input("Deseja continuar:[S/N] ")).strip().upper()[0]
# while continuar != "N":
#     n = int(input("Digite um número: "))
#     count += 1
#     mediacalc += n
#     if maior < n:
#         maior = n
#     elif menor > n:
#         menor = n
#     continuar = str(input("Deseja continuar:[S/N] ")).strip().upper()[0]
#     while continuar not in "SN":
#         print("Opção inexistente.")
#         continuar = str(input("Deseja continuar:[S/N] ")).strip().upper()[0]
# média = mediacalc / count
# print("A média entre os números digitados é: {:.2f}".format(média))
# print("O maior número digitado foi {} e o menor número {}".format(maior, menor))

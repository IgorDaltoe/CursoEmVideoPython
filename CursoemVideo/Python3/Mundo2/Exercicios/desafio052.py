n = int(input("Digite um número inteiro: "))
primo = bool(True)
for c in range (2, n):
    if n % c == 0:
        primo = False
if n == 1:
    print("O número {} não é primo.".format(n))
elif primo == True:
    print("O número {} é primo.".format(n))
elif primo == False:
    print("O número {} não é primo.".format(n))

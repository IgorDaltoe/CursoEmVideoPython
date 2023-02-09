num = int(input("Digite um número inteiro: "))
print("""Escolha uma das bases para conversão: 
[ 1 ] Converter para BINÁRIO
[ 2 ] Convertar para OCTAL
[ 3 ] Convertar para HEXADECIMAL""")
opção = int(input("Sua opção: "))
if opção == 1:
    print("{} Convertido para BINÀRIO é igual a {}".format(num, bin(num)[2:]))
elif opção == 2:
    print("{} Convertido em OCTAL é igual a {}".format(num, oct(num)[2:]))
elif opção == 3:
    print("{} Convertido para HEXADECIMAL é igual a {}".format(num, hex(num)[2:]))
else:
    print("Opção inválida. Tente novamente.")
frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = "".join(palavras)
inverso = ""
# forma de fatiamento sem usar for
# inverso = junto[::-1]
for letra in range (len(junto) -1, -1, -1):
    inverso += junto[letra]
print("O inverso de {} é {}".format(junto, inverso))
if inverso == junto:
    print("Temos um palíndromo!")
else:
    print("A frase digitada não é um palíndromo!")

# frase = str(input("digite uma frase: ")).replace(" ","").lower()
# l = len(frase)
# t = 0
# igual = 0
# for c in range(l, 1, -1):
#     a = (frase[c-1])
#     b = (frase[t])
#     if a == b:
#         igual += 1
#     t += 1
# if igual == l-1:
#     print("A frase é um palíndromo")
# else:
#     print("A frase não é um palíndromo")
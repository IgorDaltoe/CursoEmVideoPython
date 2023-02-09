primeitoTermo = int(input("Digite o primeiro termo da PA: "))
razão = int(input("Digite a razão dessa PA: "))
décimoTermo = primeitoTermo + (10 - 1) * razão
print("Os 10 primeiros termos dessa PA são:")
for c in range(primeitoTermo, décimoTermo + razão, razão):
    print(c, end=" ")

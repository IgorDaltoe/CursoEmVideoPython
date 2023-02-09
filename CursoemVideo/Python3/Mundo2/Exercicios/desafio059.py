from time import sleep
print("Por favor digite dois valores!")
n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
opção = 0
soma = 0
multiplicação = 0
maiorValor = 0
while opção != 5:
    opção = int(input("""Opções disponiveis:
[1] Somar
[2] Multiplicar
[3] Mostrar maior
[4] Selecionar novos números
[5] Fechar programa
Opção: """))
    if opção == 1:
        soma = n1 + n2
        print("\033[32mO A resultado de {} + {} é {}\033[m".format(n1, n2, soma))
        sleep(2)
    elif opção == 2:
        multiplicação = n1 * n2
        print("\033[34mO O resultado de {} x {} é {}\033[m".format(n1, n2, multiplicação))
        sleep(2)
    elif opção == 3:
        if n1 > n2:
            maiorValor = n1
        else:
            maiorValor = n2
        print("\033[33mO maior valor entre {} e {} é {}\033[m".format(n1, n2, maiorValor))
        sleep(2)
    elif opção == 4:
        print("Por favor digite novos valores:")
        n1 = int(input("Primeiro valor: "))
        n2 = int(input("Segundo valor: "))
        print("Novos valorés selecionados!")
        sleep(2)
    elif opção not in (1, 2, 3, 4, 5):
        print("\033[31mOpção invalida, por favor digite novamente!\033[m")
        sleep(2)
    elif opção == 5:
        print("\033[31mO programa será encerrado!\033[m")
        sleep(2)

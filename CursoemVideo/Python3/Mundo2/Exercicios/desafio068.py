from random import randint
from time import sleep
vic = 0
print("_-=-"*12)
print("Vamos brincar de par ou ímpar!")
print("_-=-"*12)
sleep(1)
while True:
    jgescolhe = " "
    while jgescolhe not in "PI":
        jgescolhe = str(input("Par ou Ímpar ? [P/I] ")).strip().upper()[0]
    pcnum = randint(1, 10)
    jgnum = (int(input("Digite um número: ")))
    print("_-=-"*12)
    sleep(1)
    resultado = pcnum + jgnum
    print(f"Você escolheu {jgnum} e o computador escolheu {pcnum}. Total de {resultado}.")
    if jgescolhe == "P":
        if resultado % 2 == 0:
            print("Deu PAR, Você venceu! Vamos para a proxima rodada!")
        else:
            print("Deu Ímpar, Eu venci!")
            print("_-=-"*12)
            break 
    elif jgescolhe == "I":
        if resultado % 2 != 0:
            print("Deu Ímpar, Você venceu! Vamos para a proxima rodada!")
        else:
            print("Deu Par, Eu venci!")
            print("_-=-"*12)    
            break
    vic += 1
    print("_-=-"*12)
sleep(1)
print(f"GAME OVER! Você venceu {vic} vezes).")
print("_-=-"*12)

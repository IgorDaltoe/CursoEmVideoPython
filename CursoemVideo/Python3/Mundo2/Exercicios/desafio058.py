from random import randint
from time import sleep
computador = randint(0, 10)
palpites = 1
print("-=-" * 20)
print("Vou pensar em um número de 0 a 10. Tente adivinhar...")
print("-=-" * 20)
jogador = int(input("Em qual número eu pensei ? "))
print('PROCESSANDO...')
sleep(2)
while jogador != computador:
    if jogador < computador:
        print("Você errou, tente um número... maior!")
    elif jogador > computador:
        print("Você errou, tente um número... menor!")
    # print("Você errou, tente novamente!")
    jogador = int(input("Em qual número eu pensei ? "))
    palpites += 1
    print("PROCESSANDO...")
    sleep(2)
# if jogador == computador:
print("PARABÉNS! você conseguiu me vencer!\nEu pensei no número {}, Você acertou com {} tentativas.".format(computador, palpites))

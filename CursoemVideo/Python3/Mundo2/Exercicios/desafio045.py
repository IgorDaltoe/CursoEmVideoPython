from random import randint
print("+=+" * 17)
print("Vamos jogar Pedra, papel e tesoura!")
computador = randint(0,2)
if computador == 0:
    jokenpo = ("Pedra")
elif computador == 1:
    jokenpo = ("Papel")
elif computador == 2:
    jokenpo = ("Tesoura")
jogador = str(input("Pedra, papel ou tesoura !?\n")).strip().capitalize()
print("Computador: {}!".format(jokenpo))
if jokenpo == jogador:
    print("Empatamos!")
elif computador == 0 and jogador == ("Papel"):
    print("Papel ganha de Pedra! Parabéns, você ganhou!!")
elif computador == 0 and jogador == ("Tesoura"):
    print("Pedra ganha de tesoura! Eu ganhei!!")
elif computador == 1 and jogador == ("Pedra"):
    print("Papel ganha de Pedra! Eu ganhei!!")
elif computador == 1 and jogador == ("Tesoura"):
    print("Tesoura ganha de Papel! Parabéns, você ganhou!!")
elif computador == 2 and jogador == ("Pedra"):
    print("Pedra ganha de Tesoura! Parabéns, você ganhou!!")
elif computador == 2 and jogador == ("Papel"):
    print("Tesoura ganha de Papel! Eu ganhei!!")
else:
    print("JOGADA INVÁLIDA!")
print("+=+" * 17)

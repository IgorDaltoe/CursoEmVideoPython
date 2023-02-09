# import random
# num = random.randint(0, 5)
# n = int(input('Digite um número de 0 a 5: '))
# if n == num:
#    print('Você venceu!')
# else:
#    print('Você perdeu!')
# print('o número era {}.'.format(num))
from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei ? '))
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('PARABÉNS! Eu pensei no número {}, você conseguiu me vencer!'.format(computador))
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))

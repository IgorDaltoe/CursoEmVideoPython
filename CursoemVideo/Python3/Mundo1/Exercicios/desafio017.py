'''print('Vamos calcular o comprimento da hipotenusa de um triangulo retangulo.')
c1 = float(input('Qual é o comprimento do cateto oposto ? '))
c2 = float(input('Qual é o cimprimento do cateto adjacente ? '))
h = ((c1 ** 2) + (c2 ** 2)) ** (1/2)
print('O triangulo retangulo com possui o cateto oposto {}'.format(c1))
print('O cateto adjacente {}'.format(c2))
print('E a hipotenusa {:.2f}'.format(h))'''

import math
c1 = float(input('Qual é o comprimento do cateto oposto ? '))
c2 = float(input('Qual é o cimprimento do cateto adjacente ? '))
h = math.hypot(c1, c2)
print('O triangulo retangulo com possui o cateto oposto {}'.format(c1))
print('O cateto adjacente {}'.format(c2))
print('E a hipotenusa {:.2f}'.format(h))

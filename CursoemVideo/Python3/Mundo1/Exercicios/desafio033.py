'''n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceito número: '))
# num = [n1, n2, n3]
# num.sort()
# print('O maior número é {}.'.format(num[2]))
# print('O menor número é {}.'.format(num[0]))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O menor número é {}'.format(menor))
print('O maior número é {}'.format(maior))'''
A = int(input('Digite um valor: '))
B = int(input('Digite um segundo valor: '))
C = int(input('Digite um terceiro valor: '))
D = int(input('Digite um quarto valor: '))
num = [A, B, C, D]
num.sort()
print(' \033[34m O maior valor é {}.\033[m '.format(max(num)))
print(' \033[32m O menor valor é {}.\033[m '.format(min(num)))

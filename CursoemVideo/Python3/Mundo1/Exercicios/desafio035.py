print('Vamos tentar formar um triângulo!')
n1 = float(input('Digite o comprimentos de uma semirreta: '))
n2 = float(input('Digite o comprimenro de outra semirreta: '))
n3 = float(input('Digite o comprimento de mais uma semirreta: '))
retas = [n1, n2, n3]
retas.sort()
menor = retas[0] + retas[1]
maior = retas[2]
if menor > maior:
    print('Essas semirretas conseguem formar um triângulo!')
else:
    print('Essas semirretas não conseguem formar um triângulo!')

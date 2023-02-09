num = int(input('Digite um número: '))
conta = num % 2
if conta == 0:
    print('{} é um número PAR'.format(num))
else:
    print('{} é um número IMPAR'.format(num))

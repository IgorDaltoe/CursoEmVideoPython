# nome = str(input('Digite o nome de uma cidade: '))
# print('SANTO' in nome.upper().split()[0])
nome = str(input('Digite o nome de uma cidade: ')).strip()
print(nome[:5].upper() == 'SANTO')

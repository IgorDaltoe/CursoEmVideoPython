sal = float(input('Qual é o salário do funcionário ? R$'))
#if sal > 1250:
#    print('Seu salário é de R${} e você receberá um aumento de 10%!'.format(sal))
#    print('Seu novo salário será R${:.2f}!'.format(sal + (sal * 10 / 100)))
#else:
#    print('Seu salário é de R${} e você receberá um aumento de 15%!'.format(sal))
#    print('Seu novo salário será R${:.2f}!'.format(sal + (sal * 15 / 100)))
if sal > 1250:
    novo = sal + (sal * 10 / 100)
else:
    novo = sal + (sal * 15 / 100)
print('Quem ganhava R${:.2f} passará a ganhar R${:.2f}!'.format(sal, novo))

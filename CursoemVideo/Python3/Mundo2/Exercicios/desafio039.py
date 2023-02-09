import datetime
esseAno = datetime.date.today().year
print("""O alistamento militar é obrigatório para todos os homens!
Você é Homen ou Mulher ?
[ 1 ] Homen
[ 2 ] Mulher""")
opção = int(input("Opção: "))
if opção == 2:
    print("Por ser Mulher o seu alistamento não é Obrigatório")
else:
    print("Por ser Homen seu alistamento é obrigatório")
    
ano = int(input("Em qual ano você nasceu ? "))
idade = esseAno - ano
passou = idade - 18
faltam = 18 - idade
anoAlistamento = ano + 18
print("Você que nasceu em {} tem {} anos em {}.".format(ano, idade, esseAno))
    
if idade == 18:
    print("Você deve se alistar IMEDIATAMENTE!")
elif idade > 18:
    print("Você devia te se alistado há {} ano(s).".format(passou))
    print("Seu alistamento foi em {}.".format(anoAlistamento))
elif idade < 18:
    print("Ainda falta(m) {} ano(s) para você se alistar.".format(faltam)) 
    print("Seu alistamento será em {}".format(anoAlistamento))

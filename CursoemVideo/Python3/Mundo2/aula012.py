nome = str(input("qual é o seu nome? ")).title().strip()
if nome == "Igor":
    print("Que nome bonito!")
elif nome == "Pedro" or nome == "Maria" or nome == "Paulo":
    print("Seu nome é bem comun no Brasil.")
elif nome in "Ana, Cláudia, Jéssica":
    print("Belo nome feminino")
else:
    print("Seu nome é bem normal.")
print("Tenha um bom dia {}".format(nome))
           
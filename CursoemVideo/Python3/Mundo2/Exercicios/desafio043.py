print("Vamos calcular o seu IMC!")
peso = float(input("Digite o seu peso (kg): "))
altura = float(input("Digite a sua altura (m): "))
imc = peso / (altura ** 2)
if imc < 18.5:
    imcSua = "Abaixo do peso"
elif 18.5 <= imc < 25:
    imcSua = "Peso ideal"
elif 25 <= imc < 30:
    imcSua = "Sobrepeso"
elif 30 <= imc < 40:
    imcSua = "Obesidade"
elif imc >= 40:
    imcSua= "Obesidade mórbida"
print("Seu IMC é: {:.1f}. {}".format(imc, imcSua))
    
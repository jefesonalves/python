# Prática 11 IMC
peso = float(input("Digite o seu peso (KG): "))
altura = float(input("Digite a sua altura (m): "))

imc = peso / (altura**2)

if (imc < 18.5):
    print("Abaixo do peso")
elif (imc >= 18.5) and (imc <= 25):
    print("Seu IMC,", imc, "Peso ideal")
elif (25 < imc < 30):
    print("Seu IMC,", imc, "Sobrepeso")
elif (30 < imc <= 40):
    print("Seu IMC,", imc, "Obesidade")
else:
    print("Seu IMC,", imc, "Obesidade móbida")
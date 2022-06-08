peso = float(input("Digite o peso: "))
altura = float(input("Digite a altura: "))

imc = peso / altura**2

if imc < 18.5:
    print("Abaixo do peso.")
elif imc >= 18.5 and imc <= 25:
    print("Peso normal.")
elif imc >= 25 and imc <= 30:
    print("Acima do peso.")
elif imc > 30:
    print("Obeso.")
else:
    print("Fim")
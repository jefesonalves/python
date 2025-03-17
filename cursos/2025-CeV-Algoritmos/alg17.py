velocidade = float(input("Velocidade do carro: "))
limite = 80
multa_km = 5 * 1

if (velocidade > limite):
    multa = (velocidade - limite) * multa_km
    print("O valor da multa é: R$", multa)
else:
    print("Dentro do limite regulamentar")
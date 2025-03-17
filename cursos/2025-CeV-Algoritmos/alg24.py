distancia = float(input("Distância a ser percorrida: "))


if (distancia <= 200):
    preco_passagem = distancia * 0.50
    print("Preço da passagem: ", preco_passagem)
elif (distancia > 200):
    preco_passagem = distancia * 0.45
    print("Preço da passagem: ", preco_passagem)
else:
    print("Distância inválida!")
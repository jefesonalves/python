pesos = []
alturas = []
pessoas = 7
i = 1
peso_50_altura_160 = 0
altura_190_peso_100 = 0

while (i <= 2):
    peso = float(input(f"Digite o peso da {i}ª pessoa: "))
    pesos.append(peso)
    altura = float(input(f"Digite a altura da {i}ª pessoa: "))
    alturas.append(altura)
    i += 1

    if(peso < 50 and altura < 1.6):
        peso_50_altura_160 += 1

    if(altura > 1.90 and peso > 100):
        altura_190_peso_100 += 1

media_altura_grupo = sum(alturas) / len(alturas)
mais_90kg = len([num for num in pesos if num > 90])

print(f"Média de altura do grupo: {media_altura_grupo}")
print(f"Pessoas com mais de 90kg: {mais_90kg}")
print(f"Pessoas que pesam menos de 50Kg e tem menos de 1.60m: {peso_50_altura_160}")
print(f"Pessoas que medem mais de 1.90m pesam mais de 100Kg: {altura_190_peso_100}")
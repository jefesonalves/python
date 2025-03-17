import random

numeros = []
contador = 0

while contador < 20:
    numero = random.randint(0, 10)
    numeros.append(numero)
    contador += 1
print(f"Números sorteados: {numeros}")

acima_de_5 = 0
i = 0
while i < len(numeros):
    if numeros[i] > 5:
        acima_de_5 += 1
    i += 1
print(f"Números acima de 5: {acima_de_5}")

divisiveis_por_3 = 0
i = 0
while i < len(numeros):
    if numeros[i] % 3 == 0:
        divisiveis_por_3 += 1
    i += 1
print(f"Números divisíveis por 3: {divisiveis_por_3}")
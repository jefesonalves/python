numeros = []
posicao = []
qtd_numeros = 15
multiplo = 10

for i in range(qtd_numeros):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)
    posicao.append(i)

print("--------------------------------------------")
print(f"Números armazenados no vetor:\n {numeros}")

for i in range(qtd_numeros):
    if (numeros[i] % multiplo == 0):
        print(f"Número múltiplo de {multiplo}: {numeros[i]} está na posição: {posicao[i]}")
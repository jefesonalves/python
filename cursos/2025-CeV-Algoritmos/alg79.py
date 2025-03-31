numeros = []
numeros_pares = []
posicao = []
for i in range(10):
    numero = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(numero)
    if numeros[i] % 2 == 0:
        numeros_pares.append(numeros[i])
        posicao.append(i)
        
print(f"Números digitados: {numeros}")
print(f"Números pares: {numeros_pares}")
print(f"Os números pares estão na posição: {posicao}")
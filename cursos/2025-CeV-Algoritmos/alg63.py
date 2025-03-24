numeros = []

while True:
    numero = int(input("Digite a idade: "))
    numeros.append(numero)

    continua = input("Deseja continuar (S/N)? ").upper()
    if continua != "S":
        break

valor_total = sum(numeros)
menor_numero = min(numeros)
media_total = valor_total / len(numeros)
qtd_pares = len([i for i in numeros if i % 2 == 0])

print(f"Somatório de todos os valores: {valor_total}")
print(f"Menor valor digitado: {menor_numero}")
print(f"Média dos valores: {media_total}")
print(f"Quantidade de números pares: {qtd_pares}")
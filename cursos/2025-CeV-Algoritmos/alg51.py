precos = []
i = 1

while (i <= 8):
    preco = float(input(f"Digite o preço do {i}º produto: "))
    precos.append(preco)
    i += 1

maior = max(precos)
menor = min(precos)
print(f"Maior R$: {maior}")
print(f"Menor R$: {menor}")
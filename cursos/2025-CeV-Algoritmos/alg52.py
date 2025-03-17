idades = []
pessoas = 5
i = 1
maior_18 = 0
menor_5 = 0

while (i <= pessoas):
    idade = int(input(f"Digite o preço do {i}º produto: "))
    idades.append(idade)
    if (idade > 18):
        maior_18 += 1
    if (idade < 5):
        maior_18 += 1
    i += 1

media = sum(idades) / len(idades)
maior = max(idades)
print(f"Média: {media}")
print(f"Maior de 18: {maior_18}")
print(f"Menor de 5: {menor_5}")
print(f"Maior idade: {maior}")
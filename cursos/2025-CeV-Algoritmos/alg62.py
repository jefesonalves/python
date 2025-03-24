idades = []

while True:
    idade = int(input("Digite a idade: "))
    idades.append(idade)

    continua = input("Deseja continuar (S/N)? ").upper()
    if continua != "S":
        break

total_idades = len(idades)
media_idade = sum(idades) / len(idades)
maiores_21 = len([i for i in idades if i >= 21])

print(f"Foram digitadas {total_idades} idades")
print(f"Média de idades: {media_idade}")
print(f"Maiores de 21: {maiores_21}")
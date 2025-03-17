idadeH = []
idadeM = []
sexoH = []
sexoM = []
pessoas = 4
i = 1

while (i <= pessoas):
    idade = int(input(f"Digite a idade da {i}ª pessoa: "))
    sexo = input(f"Digite o sexo da {i}ª pessoa (H) ou (M): ")
    if (sexo == "H" or sexo == "h"):
        sexoH.append(sexo)
        idadeH.append(idade)
    if (sexo == "M" or sexo == "m"):
        sexoM.append(sexo)
        idadeM.append(idade)
    i += 1

total_homem = len(sexoH)
total_mulher = len(sexoM)
media_idade_grupo = (sum(idadeH) + sum(idadeM)) / 2
media_idade_homens = sum(idadeH) / len(idadeH)
mulheres_mais_20 = len([num for num in idadeM if num > 20])

print(f"Homens cadastrados: {total_homem}")
print(f"Homens cadastrados: {total_mulher}")
print(f"Média de idade do grupo: : {media_idade_grupo}")
print(f"Média de idade dos homens: : {media_idade_homens}")
print(f"Mulheres com mais de 20 anos: : {mulheres_mais_20}")
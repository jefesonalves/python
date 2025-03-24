nomes = []
idades = []
sexos = []
sexos_m = []
sexos_f = []
idades_m = []
idades_f = []

while True:
    nome = input("Digite um nome: ").upper()
    nomes.append(nome)

    idade = int(input("Digite a idade: "))
    idades.append(idade)

    sexo = input("Digite o sexo: ").upper()
    sexos.append(sexo)

    if(sexo == "m" or sexo == "M"):
        sexos_m.append(nome)
        idades_m.append(idade)

    if(sexo == "f" or sexo == "F"):
        sexos_f.append(nome)
        idades_f.append(idade)

    continua = input("Deseja continuar (S/N)? ").upper()
    if continua != "S":
        break

maior_idade = max(idades)
indice_maior = idades.index(max(idades))

menor_idade = min(idades_f)
indice_menor = idades.index(min(idades_f))

media_idade = sum(idades) / len(idades)
homens_mais_30 = len([i for i in idades_m if i > 30])
mulheres_menos_18 = len([i for i in idades_f if i < 18])

print(f"A pessoa mais velha é {nomes[indice_maior]} com {maior_idade} anos")
print(f"A mulher mais jovem é {nomes[indice_menor]} com {menor_idade} anos")
print(f"A média de idade do grupo é: {media_idade}")
print(f"Homens com mais de 30 anos: {homens_mais_30}")
print(f"Mulheres menores de 18 anos: {mulheres_menos_18}")
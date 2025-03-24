qtd_pessoas = 8
sexos_m = []
sexos_f = []
pesos_m = []
pesos_f = []

for i in range(1, qtd_pessoas + 1):
    sexo = input(f"Digite o SEXO da {i}ª pessoa (M/F): ")
    peso = int(input(f"Digite o PESO da {i}ª pessoa: "))
    if(sexo == "m" or sexo == "M"):
        sexos_m.append(sexo)
        pesos_m.append(peso)

    if(sexo == "f" or sexo == "F"):
        sexos_f.append(sexo)
        pesos_f.append(peso)

print(f"Mulheres cadastradas: {len(sexos_f)}")
print(f"Homens que pesam mais de 100 Kg: {len([i for i in pesos_m if i > 100])}")
print(f"Média de peso entre mulheres: {sum(pesos_f) / len(pesos_f)} Kg")
print(f"Maior peso entre os homens: {max(pesos_m)} Kg")
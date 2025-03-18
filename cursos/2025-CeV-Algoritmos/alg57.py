continua = True
i = 1

salario_homens = 0
salario_mulheres = 0
while continua:
    sexo = input(f"Digite o sexo da {i}ª pessoa (M/F): ")
    if (sexo == "M" or sexo == "m"):
        salario = float(input(f"Digite o salário da {i}ª pessoa: "))
        salario_homens += salario

    if (sexo == "F" or sexo == "f"):
        salario = float(input(f"Digite o salário da {i}ª pessoa: "))
        salario_mulheres += salario

    continua = input("Deseja continuar (S/N)? ")
    if (continua == "s" or continua == "S"):
        continua == True
    else:
        break
    i += 1

print(f"Salário total das Mulheres R$ {salario_mulheres:.2f}")
print(f"Salário total dos Homens R$ {salario_homens:.2f}")
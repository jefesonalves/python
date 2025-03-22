quant_homens = 0
maior_idade = 0
mulher_mais_jovem = 9999
soma_idade_homem = 0
media_idade_homem = 0

while True:
    sexo = input("Digite o sexo (M/F): ").upper()
    if sexo not in ["M", "F"]:
        print("Opção inválida! Digite 'M' ou 'F'.")
        continue

    idade = int(input("Digite uma idade entre 1 e 120: "))
    if (idade < 1 or idade > 120):
        print("Valor errado! Digite a idade entre 1 e 120.")
        continue

    if (idade > maior_idade):
        maior_idade = idade

    if (sexo == "M"):
        quant_homens += 1
        soma_idade_homem += idade

    if (sexo == "F" and idade < mulher_mais_jovem):
        mulher_mais_jovem = idade
    
    continua = input("Deseja continuar (S/N)? ").upper()
    if continua != "S":
        break

if (quant_homens > 0):
    media_idade_homem = soma_idade_homem / quant_homens
else:
    media_idade_homem = "Nenhum homem cadastrado."

if (mulher_mais_jovem < 9999):
    mulher_mais_jovem = mulher_mais_jovem
else:
    mulher_mais_jovem = "Nenhuma mulher cadastrada." 

print(f"Maior idade digitada: {maior_idade}")
print(f"Homens cadastrados: {quant_homens}")
print(f"Idade da mulher mais jovem: {mulher_mais_jovem}")
print(f"Média da idade dos homens: {media_idade_homem}")
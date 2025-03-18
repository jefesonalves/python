continua = True
soma_idades = 0
i = 1
while continua:
    idade = int(input(f"Digite a idade do {i}º aluno: "))
    if (idade == 999):
        i = i - 1
        break
    else:
        soma_idades = soma_idades + idade
        i += 1

media_idades = soma_idades / i
print(f"Quantidade de alunos: {i}")
print(f"Média de alunos: {media_idades}")
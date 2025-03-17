ano_nascimento = int(input("Ano de nascimento: "))
ano_atual = int(input("Ano de atual: "))

idade = ano_atual - ano_nascimento
idade_min_votar = 18

if (idade >= idade_min_votar):
    print("Possui", idade, "anos e pode votar!")
else:
    print("Possui", idade, "anos e não pode votar!")
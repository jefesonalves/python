ano_nascimento = int(input("Ano nascimento: "))
ano_atual = int(input("Ano atual: "))

idade_limite = 18
idade = ano_atual - ano_nascimento

if (idade < idade_limite ):
    diferenca = idade_limite - idade
    print("Você não esta apto, faltam", diferenca, "ano(s)")
else:
    diferenca = idade - idade_limite
    print("Você esta apto e com", idade, "anos")
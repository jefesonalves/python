nome = input("Digite o nome: ")
salario = float(input("Digite o salário: "))
anos_trabalhados = int(input("Anos trabalhados: "))

if (anos_trabalhados <= 3):
    aumento = salario * 3 / 100
    salario = salario + aumento
    print(nome, "Seu novo salário é de R$", salario)
elif (3 < anos_trabalhados <= 10):
    aumento = salario * 12.5 / 100
    salario = salario + aumento
    print(nome, "Seu novo salário é de R$", salario)
elif (anos_trabalhados > 10):
    aumento = salario * 10 / 100
    salario = salario + aumento
    print(nome, "Seu novo salário é de R$", salario)
else:
    print("Dados incorretos!")
valor_casa = float(input("Digite o valor da casa: "))
salario_comprador = float(input("Digite o salario do comprador: "))
qtd_anos = int(input("Em quantos anos será paga? "))

meses = qtd_anos * 12
valor_prestacao = valor_casa / meses
limite_prestacao = salario_comprador * 30 / 100

if (valor_prestacao > limite_prestacao):
    print("Valor da prestação: ", valor_prestacao)
    print("Limite da prestação: ", limite_prestacao)
    print("Empréstimo negado!")
else:
    print("Valor da prestação: ", valor_prestacao)
    print("Limite da prestação: ", limite_prestacao)
    print("Empréstimo aprovado!")
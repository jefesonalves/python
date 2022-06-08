salario = float(input("Digite o salário: "))
percentual = float(input("Digite o percentual de aumento: "))
percentual = percentual / 100 + 1
novo_salario = salario * percentual

print("Novo salário: %.2f " %novo_salario)
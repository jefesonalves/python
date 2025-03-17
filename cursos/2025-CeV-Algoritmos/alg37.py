salario_atual = float(input("Salário atual: "))
print("1 - Mulher")
print("2 - Homem")
genero = int(input("Digite a opção: "))
anos_trabalhados = int(input("Anos trabalhados: "))

if (genero == 1 and anos_trabalhados < 15):
    novo_salario = salario_atual + salario_atual * 5 / 100
    print ("Salário atual:", novo_salario)
elif (genero == 1 and 15 <= anos_trabalhados <= 20):
    novo_salario = salario_atual + salario_atual * 12 / 100
    print ("Salário atual:", novo_salario)
elif (genero == 1 and anos_trabalhados > 20):
    novo_salario = salario_atual + salario_atual * 23 / 100
    print ("Salário atual:", novo_salario)
elif (genero == 2 and anos_trabalhados < 20):
    novo_salario = salario_atual + salario_atual * 3 / 100
    print ("Salário atual:", novo_salario)
elif (genero == 2 and 20 <= anos_trabalhados <= 30):
    novo_salario = salario_atual + salario_atual * 13 / 100
    print ("Salário atual:", novo_salario)
elif (genero == 2 and anos_trabalhados > 30):
    novo_salario = salario_atual + salario_atual * 25 / 100
    print ("Salário atual:", novo_salario)
else:
    print ("Opção inválida!")
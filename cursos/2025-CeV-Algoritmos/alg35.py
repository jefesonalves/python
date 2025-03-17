aluguel_dia_popular = 90
aluguel_dia_luxo = 150
km_dia_ate_100_popular = 0.20
km_dia_maior_100_popular = 0.10
km_dia_ate_200_luxo = 0.30
km_dia_acima_200_luxo = 0.25

print("1 - Carro popular")
print("2 - Carro de luxo")
opcao_carro = int(input("Opção: "))
dias_utilizados = int(input("Dias utilizados: "))
km_utilizado = float(input("Km utilizados? "))


if (opcao_carro == 1 and km_utilizado <= 100):
    valor_total = dias_utilizados * aluguel_dia_popular + km_utilizado * km_dia_ate_100_popular 
    print ("Valor total: ", valor_total)
elif(opcao_carro == 1 and km_utilizado > 100):
    valor_total = dias_utilizados * aluguel_dia_popular + km_utilizado * km_dia_maior_100_popular 
    print ("Valor total: ", valor_total)
elif(opcao_carro == 2 and km_utilizado <= 200):
    valor_total = dias_utilizados * aluguel_dia_luxo + km_utilizado * km_dia_ate_200_luxo
    print ("Valor total: ", valor_total)
elif(opcao_carro == 2 and km_utilizado > 200):
    valor_total = dias_utilizados * aluguel_dia_luxo + km_utilizado * km_dia_acima_200_luxo
    print ("Valor total: ", valor_total)
else:
    print("Opção inválida!")
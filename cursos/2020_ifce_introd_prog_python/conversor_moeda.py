#Declaração de variáveis.
dolar = float(input("Digite a cotação do dólar: "))
real = float(input("Digite o valor em reais: "))

#Conversão de moeda.
conversao = real / dolar

#exibindo o resultado na tela.
print("\nR$ %.2f" % real + " equivale a US$ %.2f" % conversao)
preco = float(input("Informe o preço do produto (R$): "))
desconto = float(input("Informe o percentual de desconto (%): "))

valor_desconto = preco / desconto
preco_promocional = preco - valor_desconto

print(desconto, "% de desconto equivale a R$", valor_desconto)
print("Preço com desconto de", desconto, "% é de R$", preco_promocional)
def traco(qtd):
    print(qtd * "-")


def conversao():
    dolar = float(input("Digite a cotação do dólar: "))
    real = float(input("Digite o valor em reais: "))
    conversao = real / dolar
    print("\nR$ %.2f" % real + " equivale a US$ %.2f" % conversao)


conversao()


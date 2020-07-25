numero = int(input("Digite um número: "))

resto_valor = numero % 2

if resto_valor == 0:
    print("O número é par.")
elif resto_valor == 1:
    print("o valor é ímpar.")
else:
    print("Valor inválido!")
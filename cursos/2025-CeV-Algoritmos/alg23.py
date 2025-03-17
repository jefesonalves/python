nome = input("Nome: ")
sexo = input("Sexo (M) ou (F): " )
valor = float(input("Valor das compras: "))

homem = valor * 5 / 100
mulher = valor * 13 / 100

if (sexo == "m" or sexo == "M"):
    desconto = valor - homem
    print("Desconto aplicado R$", desconto)
elif (sexo == "f" or sexo == "F"):
    desconto = valor - mulher
    print("Desconto aplicado R$", desconto)
else:
    print("Sexo inválido!")
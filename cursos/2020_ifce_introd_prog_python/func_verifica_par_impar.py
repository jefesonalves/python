def traco(qtd):
    print(qtd * "-")

def parimpar():    
    numero = int(input("Digite um número: "))
    resto = numero % 2    

    if resto == 0:
        traco(16)
        print("O número é par.")
        traco(16)
    elif resto == 1:
        traco(17)
        print("o valor é ímpar.")
        traco(17)
    else:
        traco(15)
        print("Valor inválido!")
        traco(15)


parimpar()
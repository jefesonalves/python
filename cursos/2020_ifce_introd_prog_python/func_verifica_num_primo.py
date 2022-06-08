def traco(qtd):
    print(qtd * "-")

def verificarPrimo():
    numero = int(input("Digite o numero: "))
    div = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            div = div + 1
    if div == 2:
        traco(17)
        print("O número é primo.")
        traco(17)
    else:
        traco(20)
        print("O número não é primo")
        traco(20)

verificarPrimo()
def traco(qtd):
    print(qtd * "-")


def maior():
    maior = a[0]
    for valor in a:
        if valor > maior:
            maior = valor
    traco(30)
    print("O maior número da lista é: {}".format(maior))
    traco(30)


def menor():
    menor = a[0]
    for valor in a:
        if valor < menor:
            menor = valor    
    print("O menor número da lista é: {}".format(menor))
    traco(30)


a = [2, 13, 7, 1, 17, 4, 8, 10, 6, 15]

maior()
menor()
inicio = int(input("Digite o valor: "))
fim = 1

while (inicio >= fim):
    if (inicio % 4 == 0):
        print(f"[{inicio}]", end=" ")
    else:
        print(inicio, end=" ")
    inicio = inicio - 1
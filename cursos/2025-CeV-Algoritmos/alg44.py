inicio = int(input("valor inicial: "))
fim = int(input("valor final: "))
incremento = int(input("Digite o incremento: "))

print("Contagem: ", end="")

if (inicio <= fim):
    while (inicio <= fim):
        print (inicio, end=" ")
        inicio = inicio + incremento
# (inicio >= fim):
else:
    while (inicio >= fim):
        print (inicio, end=" ")
        inicio = inicio - incremento
print("Acabou!")
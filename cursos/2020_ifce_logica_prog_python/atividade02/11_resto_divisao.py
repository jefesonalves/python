a = int(input("Digite o valor: "))

for i in range(2, 10):
    resultado = a % i
    print(f"O resto da divisão de {a} por {i} é igual a: {resultado}")
a = float(input("Digite o lado a: "))
b = float(input("Digite o lado b: "))
c = float(input("Digite o lado c: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    print("Forma um triângulo.")
else:
    print("Não forma um triângulo.")
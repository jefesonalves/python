a = float(input("Digite o lado a: "))
b = float(input("Digite o lado b: "))
c = float(input("Digite o lado c: "))

if (a == b and a == c and b == c):
    print ("Triângulo Equilátero")
elif (a == b or a == c or b == c):
    print ("Triângulo Isóceles")
elif (a != b and a != c or b != c):
    print ("Triângulo Escaleno")
import math
lado = float(input("Digite o valor do lado: "))

area = math.pow(lado,2) * math.sqrt(3) / 4
altura = lado * math.sqrt(3) / 2
print(f"A área do triângulo é igual a: {area}")
print(f"A altura do triângulo é igual a: {altura}")

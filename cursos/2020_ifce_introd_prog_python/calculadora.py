a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))

op = (input("Digite o operador soma(+), subtração(-), multiplicação(*) e divisão(/): "))

if op == "+":
    resultado = a + b
    print("{} + {} = {}".format(a, b, resultado))
elif op == '-':
    resultado = a - b
    print("{} - {} = {}".format(a, b, resultado))
elif op == '*':
    resultado = a * b
    print("{} x {} = {}".format(a, b, resultado))
elif op == '/':
    resultado = a / b
    print("{} / {} = {}".format(a, b, resultado))
else:
    print("Operador inválido")
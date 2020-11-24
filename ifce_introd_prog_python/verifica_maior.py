a = float(input("Digite o primeiro valor: "))
b = float(input("Digite o segundo valor: "))
c = float(input("Digite o terceiro valor: "))

if a > b and b > c:
    maior = a
    print("O valor maior é o A: {}".format(maior))
elif a < b and b > c:
    maior = b
    print("O valor maior é o B: {}".format(maior))
elif a < b and b < c:
    maior = c
    print("O valor maior é o C: {}".format(maior))
else:
    print("Valores são iguais")
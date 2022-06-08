a = [2, 13, 7, 1, 17, 4, 8, 10, 6, 15]

maior = a[0]
for valor in a:
    if valor > maior:
        maior = valor

menor = a[0]
for valor in a:
    if valor < menor:
        menor = valor

print("O maior número da lista é: {}".format(maior))
print("O menor número da lista é: {}".format(menor))
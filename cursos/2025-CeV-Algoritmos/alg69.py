a1 = int(input("Digite o primeiro termo da PA: "))
r = int(input("Digite a razão da PA: "))
lista = []

for i in range(0, 10):
    pa = a1 + i * r
    lista.append(pa)

print(f"Os 10 primeiros termos da PA são: {lista}")
print(f"A soma dos 10 primeiros termos é: {sum(lista)}")
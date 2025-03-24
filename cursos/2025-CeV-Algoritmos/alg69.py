a1 = int(input("Digite o primeiro termo da PA: "))
r = int(input("Digite a razão da PA: "))
qtd_elementos = 10

for i in range(1, qtd_elementos):
# pa = [a1 + i * r for i in range(10)]
    pa = a1 + (qtd_elementos - 1) * r

# total = sum(pa)

print("Os 10 primeiros termos da PA são:", pa)
# print("A soma dos 10 primeiros termos é:", total)
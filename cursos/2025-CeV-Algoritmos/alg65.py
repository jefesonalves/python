numeros = []
inicio = 100
fim = -1
saltos = -10
i = 100
mensagem = "Acabou!"

for i in range(inicio, fim, saltos):
    numeros.append(i)

print(*numeros, mensagem)
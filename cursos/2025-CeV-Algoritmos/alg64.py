numeros = []
inicio = 0
fim = 46
saltos = 5
i = 0
mensagem = "Acabou!"

for i in range(inicio, fim, saltos):
    numeros.append(i)

print(*numeros, mensagem)
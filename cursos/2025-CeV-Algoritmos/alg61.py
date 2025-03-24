i = 0
numeros = []
saltos = 3
mensagem = "Acabou!"

while i <= 30:
    numeros.append(i)
    i += 3
    
print(*numeros, mensagem)
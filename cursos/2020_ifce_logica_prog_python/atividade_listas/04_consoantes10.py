lista_consoantes = list("bcdfghjklmnpqrstvwxyz")
consoantes = 0

for i in range(0, 10):
    letra = input("Digite uma letra: ")
    if letra in lista_consoantes:
        consoantes = consoantes + 1        
    else:
        consoantes = consoantes

print("Quantidade de consoantes: ",consoantes)
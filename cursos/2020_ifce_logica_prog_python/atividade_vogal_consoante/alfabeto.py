lista_vogais = list("aeiou")
lista_consoantes = list("bcdfghjklmnpqrstvwxyz")

letra = input("Digite uma letra: ")

#letra = letra.lower()

if letra in lista_vogais:
    print("A letra digita é uma vogal")
elif letra in lista_consoantes:
    print("A letra digitada é uma consoante")
else:
    print("Letra inválida")
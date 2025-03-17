import random
tentativas = 4
i = 1
sorteio = int(random.uniform(1, 10))

while (i < tentativas):
    print(f"Tentativa {i}")
    numero = int(input("Digite um número entre [1 e 10]: "))
    if (numero == sorteio):
        print("Você escolheu:", numero)
        print("Número sorteado:", sorteio)
        print("Você acertou!")
    elif (numero < 1 or numero > 5):
        print ("Número fora do intervalo de 1 a 5.")
    else:
        print("Você escolheu:", numero)
        print("Número sorteado:", sorteio)
        print("Você errou!")
    i += 1
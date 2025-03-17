import random
sorteio = int(random.uniform(1, 5))
numero = int(input("Digite um número entre [1 e 5]: "))

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
import random

opcoes = ["pedra", "papel", "tesoura"]
random.shuffle(opcoes)
sorteio = random.choice(opcoes)

print("Digite 1 para Pedra")
print("Digite 2 para Papel")
print("Digite 3 para Tesoura")
opcao = int(input("Opção: "))

if (opcao == 1):
    opcao = "pedra"
elif (opcao == 2):
    opcao = "papel"
elif (opcao == 3):
    opcao = "tesoura"

if (opcao == "pedra" and sorteio == "tesoura"):
    print("Você ganhou porque", opcao, "quebra a", sorteio)
elif (opcao == "papel" and sorteio == "pedra"):
    print("Você ganhou porque", opcao, "enrola a", sorteio)
elif (opcao == "tesoura" and sorteio == "papel"):
    print("Você ganhou porque", opcao, "corta o", sorteio)
elif (opcao == "tesoura" and sorteio == "pedra"):
    print("Você perdeu porque", sorteio, "quebra a", opcao)
elif (opcao == "pedra" and sorteio == "papel"):
    print("Você perdeu porque", sorteio, "enrola a", opcao)
elif (opcao == "papel" and sorteio == "tesoura"):
    print("Você perdeu porque", sorteio, "corta o", opcao)
else:
    print("Empatou, porque foi", opcao, "com", sorteio)
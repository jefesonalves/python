import random
vetor = []

for i in range(0, 7):
    sorteio = int(random.uniform(0, 7))
    teste = random.randrange(0, 7)
    vetor.append(sorteio)

print(*vetor)
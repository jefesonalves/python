vetor = []

for i in range(1, 8):
    nome = input(f"Digite o {i}º nome: ")
    vetor.append(nome)

print(*vetor[::-1])
med_batidas = 1

idade = int(input("Digite a expectativa de vida: "))

batidas_diaria = med_batidas * 24 * 3600 * 365.25
total_batidas = idade * batidas_diaria

print("Considerando a idade de ", idade, "anos o coração baterá", int(total_batidas), "vezes ao longo da vida.")
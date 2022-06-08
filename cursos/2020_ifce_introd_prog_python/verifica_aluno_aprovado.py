media_final = float(input("Digite a média final: "))
perc_freq = float(input("Digite o percentual de frequência: "))
perc_freq = perc_freq / 100

if media_final >= 6 and perc_freq >= 0.75:
    print("Aluno aprovado!")
elif media_final < 6 and perc_freq >= 0.75:
    print("Aluno reporvado por nota!")
elif media_final >= 6 and perc_freq < 0.75:
    print("Aluno reporvado por falta!")
else:
    print("Aluno reprovado por falta e por nota.")
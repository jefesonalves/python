horas_atividade = float(input("Horas de atividade: "))

if (horas_atividade <= 10):
    pontos = horas_atividade * 2
    faturamento = pontos * 5
    print("Primeiro if")
    print("Pontos: ", pontos)
    print("Faturamento R$", faturamento)
elif (10 < horas_atividade < 20):
    pontos = horas_atividade * 5
    faturamento = pontos * 5
    print("segundo if")
    print("Pontos: ", pontos)
    print("Faturamento R$", faturamento)
elif (horas_atividade > 20):
    pontos = horas_atividade * 10
    faturamento = pontos * 5
    print("terceiro if")
    print("Pontos: ", pontos)
    print("Faturamento R$", faturamento)
else:
    print("Horas inválidas.")
qnt_cigarros = int(input("Fumou quantos cigarros por dia? "))
qnt_anos_fumou = int(input("Fumou por quantos anos? "))

perda_vida_minutos = qnt_cigarros * 10
dias_vida_perdido = perda_vida_minutos * 365 * qnt_anos_fumou / 1440
print("Dias de vida perdido: ", int(dias_vida_perdido))
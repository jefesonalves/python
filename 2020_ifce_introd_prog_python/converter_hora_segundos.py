hora = int(input("Digite a hora: "))
minuto = int(input("Digite o minuto: "))
segundo = int(input("Digite o segundo: "))

hora_exata_digitada = (str(hora) + ":" + str(minuto) + ":" + str(segundo))
qtd_segundos = hora * 3600 + minuto * 60 + segundo

print("O intervalo temporal", hora_exata_digitada, "corresponde a", qtd_segundos, "segundos.")
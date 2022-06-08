tam_arquivo = float(input("Digite o tamanho do arquivo em MB: "))
vel_link = int(input("Digite a velocidade do link em Mbps: "))

tam_arquivo = tam_arquivo * 1024
taxa_transferencia = vel_link * 1024 / 8 
tempo_aprox = tam_arquivo / taxa_transferencia

horas = tempo_aprox / 3600
tempo_aprox = tempo_aprox % 3600
minutos = tempo_aprox / 60
tempo_aprox = tempo_aprox % 60

print("Tempo aproximado de download:\n",int(horas),"h:",int(minutos),"m:",int(tempo_aprox),"s")
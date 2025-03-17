km_percorrido = float(input("Digite a quantidade de km percorrido: ")) 
quant_dias_alugado = int(input("Quantidade de dias: "))
valor_diaria = 90
valor_km = 0.20

total_pagar = quant_dias_alugado * valor_diaria + km_percorrido * valor_km

print("Total a pagar R$: ", total_pagar)
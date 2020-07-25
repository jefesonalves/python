numero = int(input("Digite o numero: "))
div = 0
for i in range(1, numero + 1):
	if numero % i == 0:
		div = div + 1           		    	
		
if div == 2:
    print("O número é primo.")
else:
    print("O número não é primo")
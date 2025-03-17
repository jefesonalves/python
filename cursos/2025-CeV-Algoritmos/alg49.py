i = 1
par = 0
impar = 0
while (i <= 6):
    numero = int(input(f"Digite o {i}º número: "))
    if (numero % 2 == 0):
        par = par + 1
    else:
        impar = impar + 1        
    i += 1
print (par, "números pares.")
print (impar, "números ímpares.")
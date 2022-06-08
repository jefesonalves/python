lista =  [1,2,3,4,5,6,7,9,10,11,12,13,14,15,16,17,18,19,20]

lista_num_pares = sorted(filter(lambda num: num % 2 == 0, lista))
lista_num_impares = sorted(filter(lambda num: num % 2 != 0, lista))

print("Números da lista:", lista)
print ("Números pares:", lista_num_pares)
print ("Números ímpares:", lista_num_impares)
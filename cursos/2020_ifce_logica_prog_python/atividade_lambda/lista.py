lista =  [1,2,3,4,5,6,7,9,10]

lista_num_pares = sorted(filter(lambda num: num % 2 == 0, lista))

print (lista_num_pares)
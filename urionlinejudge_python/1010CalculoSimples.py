lista1 = input().split(' ')
cod1 = int(lista1[0]) 
qtd1 = int(lista1[1])
vlr1 = float(lista1[2])

lista2 = input().split(' ')
cod2 = int(lista2[0]) 
qtd2 = int(lista2[1])
vlr2 = float(lista2[2])
totalapagar = qtd1 * vlr1 + qtd2 * vlr2
print(('VALOR A PAGAR: R$ {:.2f}'.format(totalapagar)))

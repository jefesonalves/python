'''
Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. A seguir, 
calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. 
As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. 
A seguir mostre a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).

Saída
Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme exemplo fornecido.

Obs: Utilize ponto (.) para separar a parte decimal.
'''
# valor = float(input())
valor = 4.11

notas = [100, 50, 20, 10, 5, 2]
tamanho = len(notas)

for i in range(tamanho):
    if int(valor) < (notas[i]):
        print("0 nota(s) de R$ ", notas[i],".00")
    elif int(valor) > (notas[i]):
        print("0 nota(s) de R$ ", notas[i],".00")
        

        





# parte_inteira = int(valor)
# parte_fracionada = valor - parte_inteira

# print("NOTAS:")
# parte_inteira = parte_inteira / 100
# print(parte_inteira, "nota(s) de R$ 100.00")
# resto = parte_inteira % 100
# print(resto)

# notas_cinquenta = resto / 50
# print(notas_cinquenta, "nota(s) de R$ 50.00")
# resto = resto % 50

# notas_vinte = resto / 20
# print(notas_vinte, "nota(s) de R$ 20.00")
# resto = resto % 20

# notas_dez = resto / 10
# print(notas_dez, "nota(s) de R$ 10.00")
# resto = resto % 10

# notas_cinco = resto / 5
# print(notas_cinco, "nota(s) de R$ 5.00")
# resto = resto % 5

# notas_dois = resto / 2
# print(notas_dois, "nota(s) de R$ 2.00")
# resto = resto % 2

# print("MOEDAS:")
# moeda_um = parte_fracionada / 1
# print(moeda_um, "moeda(s) de R$ 1.00")
# resto = resto % 1
# moeda_cinq_cent = resto / 0.5
# print(int(moeda_cinq_cent), "moeda(s) de R$ 0.50")
# resto = resto % 0.5

# moeda_vintecinco_cent = resto / 0.25
# print(int(moeda_vintecinco_cent), "moeda(s) de R$ 0.25")
# resto = resto % 0.25

# moeda_dez_cent = resto / 0.10
# print(int(moeda_dez_cent), "moeda(s) de R$ 0.10")
# resto = resto % 0.10

# moeda_cinco_cent = resto / 0.05
# print(int(moeda_cinco_cent), "moeda(s) de R$ 0.05")
# resto = resto % 0.05

# moeda_um_cent = resto / 0.01
# print(int(moeda_um_cent), "moeda(s) de R$ 0.01")
# resto = resto % 0.01
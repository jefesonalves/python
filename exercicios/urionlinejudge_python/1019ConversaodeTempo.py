'''
Problema 1019 Conversão de Tempo

Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.

Entrada
O arquivo de entrada contém um valor inteiro N.

Saída
Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos, conforme exemplo fornecido.
'''
segundos = int(input())
horas = (segundos // 3600)
minutos = (segundos - (horas * 3600)) // 60
segundos = (segundos % 60)
print('{0}:{1}:{2}'.format(horas,minutos,segundos))

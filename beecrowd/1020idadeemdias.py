'''
Problema 1020 Idade em Dias
Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias
Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias. Nos casos de teste nunca haverá uma situação que permite 12 meses e alguns dias, como 360, 363 ou 364. Este é apenas um exercício com objetivo de testar raciocínio matemático simples.

Entrada
O arquivo de entrada contém um valor inteiro.

Saída
Imprima a saída conforme exemplo fornecido.
'''
idade = int(input())

diasano = 365
diasmes = 30

ano = idade // diasano
mes = (idade - ano * diasano) // diasmes
dia = (idade - ano * diasano - mes * diasmes)
print(ano, "ano(s)")
print(mes, "mes(es)")
print(dia, "dia(s)")

#Desafio 10 do Curso em Vídeo
valor = float(input('Digite o valor em R$: '))
cotacao = float(input('Cotação do dólar atual: '))

conversao = valor / cotacao

print('Hoje você pode comprar {:.3f}'.format(conversao))

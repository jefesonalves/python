#Desafio 23 do Curso em Vídeo

numero = input('Digite um número de 0 a 9999: ')

validacao = int(numero)

while (validacao > 9999):
    print('Valor maior do que 9999...')
    numero = input('Digite um número de 0 a 9999: ')
    validacao = int(numero)

else:
    print('Unidade(s): {} '.format(numero[3]))
    print('Dezena(s): {} '.format(numero[2]))
    print('Centena(s): {} '.format(numero[1]))
    print('Milhar(s): {} '.format(numero[0]))
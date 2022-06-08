'''
Desafio 17 do Curso em Vídeo
Comprimento da Hipotenusa
'''

a = float(input('Digite o comprimento do cateto oposto: '))
b = float(input('Digite o comprimento do cateto adjacente: '))

a = a**2
b = b**2
soma = a + b
c = soma ** (1/2)

print('O comprimento da hipotenusa é igual a {}'.format(c))
'''
Desafio 18 do Curso em Vídeo
'''
import math

angulo = float(input('Digite o valor do ângulo: '))

radiano = math.radians(angulo)
seno = math.sin(radiano)
cosseno = math.cos(radiano)
tangente = math.tan(radiano)

print('O seno do ângulo é: {} \n O cosseno do ângulo é: {} \n A tangente do ângulo é: {}'.format(seno, cosseno, tangente))

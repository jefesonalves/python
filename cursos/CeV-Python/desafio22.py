#Desafio 22 do Curso em Vídeo
nome = input('Digite o nome completo: ')

print('Nome convertido para maiúsculo: {}'.format(nome.upper()))
print('Nome convertido para minúsculo: {}'.format(nome.lower()))

nome = nome.split()

print('Primeiro nome: {}'.format(nome[0]))
print('O primeiro nome possui {}'.format(len(nome[0])))

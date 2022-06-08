# Desafio 19 e 20(item 4 do menu) do Curso em Vídeo
import random

registro = []

while True:
    print('\nMenu de opções\n1.Cadastrar\n2.Consultar\n3.Sortear\n4.Ordenar\n5.Sair\n ')
    opcao = input('Escolha a opção: ')
    if opcao == '1':
        registro.append(input('Digite o nome: \n'))
        print('\nGravado com sucesso!')
    elif opcao == '2':
        print('\nLista dos registros: {} '.format(registro))
    elif opcao == '3':
        print('\nNome sorteado: {}'.format(random.choice(registro)))
    elif opcao == '4':
        registro.sort()
        print('Lista ordenada: {}'.format(registro))
    elif opcao == '5':
        print('\nVocê saiu do sistema...')
        exit()
    else:
        print('Opção inválida, digite opções entre 1 e 4')

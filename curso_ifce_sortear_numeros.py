import random
from datetime import datetime

now = datetime.now()

opcao = int(input('Selecione o jogo: [1] Mega Sena [2] Teste: '))

if opcao == 1:
    numeros = random.sample(range(1, 60), 6)
    print('{}-{}-{} {}:{} - Mega Sena: {}'.format(now.day, now.month, now.year, now.hour, now.minute, numeros))

elif opcao == 2:
    print('Em teste...')

else:
    print('Opção inválida!')
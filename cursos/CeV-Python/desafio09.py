# Desafio 09 do Curso em Vídeo

a = int(input('Digite o valor: '))

print('#######################')
print('# Adição        | + | #')
print('# Subtração     | - | #')
print('# Multiplicação | x | #')
print('# Divisão       | / | #')
print('#######################')

op = (input('Digite um dos operadores relacionados acima: '))

if op == '+':
    for i in range(1, 10):
        resultado = a + i
        print('{} + {} = {}'.format(a, i, resultado))
elif op == '-':
    for i in range(1, 10):
        resultado = a - i
        print('{} - {} = {}'.format(a, i, resultado))
elif op == 'x':
    for i in range(1, 10):
        resultado = a * i
        print('{} x {} = {}'.format(a, i, resultado))
elif op == '/':
    for i in range(1, 10):
        resultado = a /i
        print('{} / {} = {:.2f}'.format(a, i, resultado))
else:
    print('Não é um operador válido')
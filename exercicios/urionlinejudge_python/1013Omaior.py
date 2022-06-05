lista = input().split(' ')
a = int(lista[0])
b = int(lista[1])
c = int(lista[2])
maiorab = (a + b + abs(a - b)) / 2
maiorabc = (maiorab  + c + abs(maiorab - c)) /2
maiorabc = int(maiorabc)
print ((maiorabc), 'eh o maior')

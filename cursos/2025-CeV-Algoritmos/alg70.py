a = 0
b = 1
c = 0
lista_fib = []
for i in range(0, 10):
    lista_fib.append(a)
    c = a + b
    a = b
    b = c

print(*lista_fib,"...")
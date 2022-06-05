lista = input().split(' ')
a = float(lista[0])
b = float(lista[1])
c = float(lista[2])
pi = 3.14159
raio = c
basemaior = a
basemenor = b
altura = c
ladoquadrado = b
ladoretanguloa = a
ladoretangulob = b

areatriangulo = a * c / 2
areacirculo = pi * raio ** 2
areatrapezio = ( basemaior + basemenor) * altura / 2
areaquadrado = ladoquadrado ** 2
areadoretangulo = ladoretanguloa * ladoretangulob
print ('TRIANGULO: {:.3f}'.format (areatriangulo))
print ('CIRCULO: {:.3f}'.format (areacirculo))
print ('TRAPEZIO: {:.3f}'.format (areatrapezio))
print ('QUADRADO: {:.3f}'.format (areaquadrado))
print ('RETANGULO: {:.3f}'.format (areadoretangulo))

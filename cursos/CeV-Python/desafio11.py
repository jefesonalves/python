# Desafio 11 do Curso em Vídeo

largura = float(input("Digite a largura em m: "))
altura = float(input("Digite a altura em m: "))

eficiencia_litro_tinta = 2
area = largura * altura
qnt_litros = area / eficiencia_litro_tinta

print('Considerando que 1 litro de tinta pinta {}m².\n Para uma área de {:.2f}m² serão necessários {:.2f} litros de tinta'.format(eficiencia_litro_tinta, area, qnt_litros))


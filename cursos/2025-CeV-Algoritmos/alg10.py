largura = float(input("Digite a largura da parede: "))
altura = float(input("Digite a altura da parede: "))

area = largura * altura
rendimento = 1 * 2
tinta_necessaria = area / rendimento

print("Para a pintar a área de", area, "m2 serão necessários", tinta_necessaria, "litros de tinta")
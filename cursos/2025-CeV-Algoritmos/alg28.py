largura = float(input("Digite a largura do terreno: "))
comprimento = float(input("Digite o comprimento do terreno: "))

area = largura * comprimento

if (area < 100):
    print("Área de", area, "m² Terreno popular.")
elif (100 <= area <= 500):
    print("Área de", area, "m² Terreno Master.")
elif (area > 500):
    print("Área de", area, "m² Tereno Vip")
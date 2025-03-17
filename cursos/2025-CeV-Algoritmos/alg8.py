distancia = float(input("Digite uma distância em metros: "))

km = distancia / 1000
hm = distancia / 100
dam = distancia / 10
dm = distancia * 10
cm = distancia * 100
mm = distancia * 1000

print("A distância de", distancia, "m corresponde a:")
print(km, "Km")
print(hm, "Hm")
print(dam, "Dam")
print(dm, "dm")
print(cm, "cm")
print(mm, "mm")
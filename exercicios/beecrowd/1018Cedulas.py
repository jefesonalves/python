cem = 100
cinquenta = 50
vinte = 20
dez = 10
cinco = 5
dois = 2
um = 1

valor = int(input())

print (valor)
qtdcem = (valor // cem)
print (qtdcem, 'nota(s) de R$ 100,00')
restocem = (valor % cem)

qtdcinquenta = (restocem // cinquenta)
print (qtdcinquenta, 'nota(s) de R$ 50,00')
restocinquenta = (restocem % cinquenta)

qtdvinte = (restocinquenta // vinte)
print (qtdvinte, 'nota(s) de R$ 20,00')
restovinte = (restocinquenta % vinte)

qtddez = (restovinte // dez)
print (qtddez, 'nota(s) de R$ 10,00')
restodez = (restovinte % dez)

qtdcinco = (restodez // cinco)
print (qtdcinco, 'nota(s) de R$ 5,00')
restocinco = (restodez % cinco)

qtddois = (restocinco // dois)
print (qtddois, 'nota(s) de R$ 2,00')
restodois = (restocinco % dois)

qtdum = (restodois // um)
print (qtdum, 'nota(s) de R$ 1,00')

multiplicador = 9

multiplicando = int(input("Digite o multiplicando: "))
for multiplicador in range(1, 10):
    produto = multiplicando * multiplicador
    print(f"{multiplicando} x {multiplicador} = {produto}")
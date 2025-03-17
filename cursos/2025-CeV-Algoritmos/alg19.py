nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

nota_media = (nota1 + nota2) / 2
media = 7

if (nota_media >= media):
    print("Nota: ", nota_media)
    print("O aluno", nome, "teve um bom aproveitamento!")
else:
    print("Nota: ", nota_media)
    print("O aluno", nome, "não teve um bom aproveitamento!")
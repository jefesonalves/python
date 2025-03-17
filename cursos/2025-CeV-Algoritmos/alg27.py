nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))

media_notas = (nota1 + nota2) / 2

if (7 <= media_notas <= 10):
    print ("Aprovado com média", media_notas)
elif (5 <= media_notas <= 6.9):
    print ("Em recuperação com média", media_notas)
elif (0 <= media_notas <= 4.9):
    print ("Reprovado com média", media_notas)
else:
    print("Sem lançamento!")
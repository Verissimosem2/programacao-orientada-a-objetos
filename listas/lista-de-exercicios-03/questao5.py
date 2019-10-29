nota = float (input("primeira nota: "))
nota2 = float (input("segunda nota: "))
media = (nota+nota2)/2
if media >=7 and media <10:
    print("aprovado")
elif media <=6.9:
    print("reprovado")
elif media == 10:
    print("Aprovado com distinção")
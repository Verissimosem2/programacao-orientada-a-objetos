numero = float (input("Digite o primeiro numero: "))
numero_2 = float (input("Digite o segundo numero: "))
numero_3 = float (input("Digite o terceiro numero: "))
if numero > numero_2 and numero > numero_3:
    print("Maior: ",numero)
elif numero_2 > numero and numero_2 > numero_3:
    print("Maior: ",numero_2)
elif numero_3 > numero_2 and numero_3 > numero:
    print("Maior: ",numero_3)
if numero < numero_2 and numero < numero_3:
    print("Menor: ",numero)
elif numero_2 < numero and numero_2 < numero_3:
    print("Menor: ",numero_2)
elif numero_3 < numero_2 and numero_3 < numero:
    print("Menor: ",numero_3)
lista = ['A','E','I','O','U']
lista_2 = ['a','e','i','o','u']
letra = str (input("Digite uma letra: "))
if letra in lista:
    print("vogal")
elif letra in lista_2:
    print("vogal")
elif letra not in lista:
    print("consoante")
elif letra not in lista_2:
    print("consoante")

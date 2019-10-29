primeiro_lado = float(input("Digite o primeiro lado: "))
segundo_lado = float(input("Digite o segundo lado: "))
terceiro_lado = float(input("Digite o terceiro lado: "))
if (primeiro_lado + segundo_lado) > terceiro_lado or (primeiro_lado + terceiro_lado) > segundo_lado or (segundo_lado + primeiro_lado) > terceiro_lado or (segundo_lado + terceiro_lado) > primeiro_lado or (terceiro_lado + primeiro_lado) > segundo_lado or (terceiro_lado + segundo_lado) > primeiro_lado:
 
     if primeiro_lado == segundo_lado and primeiro_lado == terceiro_lado:
         print("Triangulo equilatero")
     elif primeiro_lado == segundo_lado or primeiro_lado == terceiro_lado or segundo_lado == terceiro_lado:
         print("Triangulo isosceles")
     elif primeiro_lado != segundo_lado and primeiro_lado != terceiro_lado and segundo_lado != terceiro_lado:
         print("Triangulo Escaleno")
else:
    ("Não pode ser triangulo")
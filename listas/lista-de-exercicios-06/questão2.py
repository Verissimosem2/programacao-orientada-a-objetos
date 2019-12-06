import random

nome = ["Kouta", "Felipe", "Sakura", "Naruto", "Sasuke", "Natsu", "Lawliet", "Eden", "Fujitora", "Ichigo", "Luffy", "Zoro", "Ussop", "Nami", "Brook", "Andrey", "Alisson", "Mineta", "Deku", "Ash", "Mist"]
sobrenome = ["Akihito", "Lopes", "Ferreira", "Silva", "Uzumaki", "Uchiha", "Dragnell", "Kurosaki", "Roronoa", "Alves", "Verissimo", "lima", "Senju", "Hyuga", "Andrade", "Barbosa", "Barros", "Campos", "Tanaka", "Yamamoto"]
numero = int(input("Digite um numero: "))

with open("nomes2", "w") as saida:
    for i in range(0, numero):
        sorteio_nome = random.randint (0, len(nome)-1)
        sorteio_sobrenome = random.randint (0, len(sobrenome)-1)
        idade = random.randint (0, 101)
        altura = random.randint(0, 230)
        altura_final = altura/100
        print ("{} {} {} {}m".format(nome[sorteio_nome], sobrenome[sorteio_sobrenome], idade, altura_final), file = saida)


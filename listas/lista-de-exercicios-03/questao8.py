produto = float(input("Preço do primeiro produto: "))
produto_2 = float(input("Preço do segundo produto: "))
produto_3 = float(input("Preço do terceiro produto: "))
if produto < produto_2 and produto < produto_3:
    print("O primeiro produto é mais barato")
elif produto_2 < produto and produto_2 < produto_3:
    print("O segundo produto é mais barato")
elif produto_3 < produto_2 and produto_3 < produto:
    print("O terceiro produto é mais barato")
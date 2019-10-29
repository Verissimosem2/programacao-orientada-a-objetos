dinheiro_hora = float(input("Quanto ganha por hora de trabalho: "))
horas_trabalho_mes = int(input("Horas de trabalho por mes: "))
sal_bruto = dinheiro_hora * horas_trabalho_mes
imposto_de_renda = sal_bruto * 0.11
inss = sal_bruto * 0.08
sindicato = sal_bruto * 0.05
sal_liquido = (((sal_bruto - imposto_de_renda)-inss)-sindicato)
print("Salario bruto: ",sal_bruto)
print("imposto de renda: ",imposto_de_renda)
print("inss: ",inss)
print("sindicato: ",sindicato)
print("salario liquido: ",sal_liquido)

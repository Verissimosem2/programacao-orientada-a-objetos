
arquivo = open('amazon.csv')

queimadas_a = 0	
queimadas_c = 0
queimadas_am = 0
queimadas_m = 0
esta = 0

print("Indice de queimadas decorrentes No Brasil")
est = input()


for linha in arquivo:
	
	linha = linha.strip('\n')
	ano, estado, mes, numero, data = linha.split(',')
	numero = numero.replace(".", "")
	estado= estado.replace('"','')

	
	if estado == 'Acre' and ano == '2015':
		queimadas_a = queimadas_a + int(numero)

	elif estado == 'Ceara' and ano == '2014':
		queimadas_c = queimadas_c + int(numero)

	elif estado == 'Amazonas':
		queimadas_am = queimadas_am + int(numero)

	elif estado == 'Mato Grosso':
		if int(ano) >= 2010: 
			queimadas_m = queimadas_m + int(numero)
	

print("Queimadas no Acre: {}".format(queimadas_a))		
print("Queimadas no Ceará: {}".format(queimadas_c))
print("Queimadas no Amazonas: {}".format(queimadas_am))
print("Queimadas no Mato Grosso: {}".format(queimadas_m))


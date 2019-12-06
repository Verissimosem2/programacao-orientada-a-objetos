nome_aluno = input('Informe o nome do aluno: ')
with open('chamada.txt', 'r') as nomes:
    lista_nomes = nomes.readlines()
    for linhas in lista_nomes:
        print(linhas)
        

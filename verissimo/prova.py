with open('usuarios.txt', 'r') as fonte:
    nomes_usuario = fonte.readline()
    print(nomes_usuario)
    indice = 0
    for divisao in fonte:
        usuario = divisao.strip()
        indice += 1



with open ('repositório.txt', 'w') as arquivo_final:
    print('ACME Inc.    ', '    Uso de espaço em disco pelos usuários', '\n',
     '-'*90, '\n',
     'Nr    ', 'Usuário     ', 'Espaço utilizado    ', '% do uso    ','\n',
     usuario,
      file = arquivo_final )    

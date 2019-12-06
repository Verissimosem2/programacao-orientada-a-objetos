def copia_texto(teste, teste2):
    with open(teste,'r') as fonte:
        saida = fonte.readlines()
        with open(teste2,'w') as receptasculo:
            index = 0
            for linhas in saida:   
                if linhas.find('//') != 0 :
                    print(saida[index].strip('\n'), file = receptasculo)
                index += 1
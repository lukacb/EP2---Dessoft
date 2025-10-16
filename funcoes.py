def define_posicoes(linha, coluna, orientacao, tamanho):
    lista_final = []

    if orientacao == "vertical":

        for nova_linha in range(linha, linha + tamanho):
            posicao = [nova_linha, coluna]
            lista_final.append(posicao)
            
    elif orientacao == "horizontal":

        for nova_coluna in range(coluna, coluna + tamanho):
            posicao = [linha, nova_coluna]
            lista_final.append(posicao)


    return lista_final
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

def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):

    novas_posicoes = define_posicoes(linha, coluna, orientacao, tamanho)

    if nome_navio in frota:

        frota[nome_navio].append(novas_posicoes)
    else:

        frota[nome_navio] = [novas_posicoes]
        
    return frota


def faz_jogada(tabuleiro, linha, coluna):

    if tabuleiro[linha][coluna] == 1:

        tabuleiro[linha][coluna] = 'X'

    else:
        tabuleiro[linha][coluna] = '-'
        
    return tabuleiro


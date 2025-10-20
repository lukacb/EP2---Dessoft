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

def posiciona_frota(frota):
    
    tabuleiro_vazio = []
    for i in range(10):
        linha_nova = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        tabuleiro_vazio.append(linha_nova)
        
    for lista_de_navios in frota.values():
        for navio in lista_de_navios:
            for posicao in navio:

                linha = posicao[0]
                coluna = posicao[1]
                tabuleiro_vazio[linha][coluna] = 1
                
    return tabuleiro_vazio

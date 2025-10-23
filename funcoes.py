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

    tabuleiro = [[0 for _ in range(10)] for _ in range(10)]

    for navio in frota:

        for posicoes in frota[navio]:

            for posicao in posicoes:

                linha = posicao[0]
                coluna = posicao[1]

                tabuleiro[linha][coluna] = 1

    return tabuleiro

def afundados(frota, tabuleiro):

    afundados = 0

    for navio in frota:

        afundado = True

        for posicoes in frota[navio]:

            for posicao in posicoes:

                linha = posicao[0]
                coluna = posicao[1]

                if tabuleiro[linha][coluna] != 'X':
                    afundado = False

        if afundado:
            afundados += 1

    return afundados

def posicao_valida(frota, linha, coluna, orientacao, tamanho):

    novas_posicoes = define_posicoes(linha, coluna, orientacao, tamanho)

    for posicao in novas_posicoes:

        nova_linha = posicao[0]
        nova_coluna = posicao[1]

        if nova_linha < 0 or nova_linha > 9 or nova_coluna < 0 or nova_coluna > 9:
            return False

        for navio in frota:

            for posicoes in frota[navio]:

                for posicao_existente in posicoes:

                    linha_existente = posicao_existente[0]
                    coluna_existente = posicao_existente[1]

                    if nova_linha == linha_existente and nova_coluna == coluna_existente:
                        return False

    return True

def jogada_valida(tabuleiro, linha, coluna):

    if linha < 0 or linha > 9 or coluna < 0 or coluna > 9:
        return False

    if tabuleiro[linha][coluna] == 'X' or tabuleiro[linha][coluna] == '-':
        return False

    return True

def ganhou_jogo(frota, tabuleiro):

    total_navios = 0
    navios_afundados = afundados(frota, tabuleiro)

    for navio in frota:
        total_navios += 1

    if navios_afundados == total_navios:
        return True
    else:
        return False
    

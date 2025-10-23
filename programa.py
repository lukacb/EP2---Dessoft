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

def afundados(frota, tabuleiro):
    navios_afundados = 0

    for nome_navio in frota:

        posicoes_navio = frota[nome_navio]

        for posicao in posicoes_navio:

            afundado = True

            for coordenada in posicao:

                linha = coordenada[0]
                coluna = coordenada[1]

                if tabuleiro[linha][coluna] != 'X':
                    afundado = False
                    break

            if afundado:
                navios_afundados += 1

    return navios_afundados

def posicao_valida(frota, linha, coluna, orienta, tamanho):

    novasposicoes = define_posicoes(linha, coluna, orienta, tamanho)

    for posicao in novasposicoes:
        linha = posicao[0]
        coluna = posicao[1]

        if linha < 0 or linha > 9 or coluna < 0 or coluna > 9:
            return False
        
        for navios in frota.values():
            for posicoes in navios:
                if posicao in posicoes:
                    return False
    
    return True

# programa.py

embarcacoes = [
    ("porta-aviões", 4, 1),
    ("navio-tanque", 3, 2),
    ("contratorpedeiro", 2, 3),
    ("submarino", 1, 4),
]

frota = {
    "porta-aviões": [],
    "navio-tanque": [],
    "contratorpedeiro": [],
    "submarino": []
}

for nome, tamanho, qtd in embarcacoes:
    colocados = 0
    while colocados < qtd:
        print(f"Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}")
        linha = int(input("Linha: "))
        coluna = int(input("Coluna: "))

        if nome == "submarino":
            orientacao = "vertical"  
        else:
            a = int(input("[1] Vertical [2] Horizontal >"))
            if a == 1:
                orientacao = "vertical"
            else:
                orientacao = "horizontal"

        if posicao_valida(frota, linha, coluna, orientacao, tamanho):
            frota = preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
            colocados += 1
        else:
            print("Esta posição não está válida!")

print(frota)






            




    




  
   

#funcoes

from funcoes import (
    define_posicoes,
    preenche_frota,
    faz_jogada,
    posiciona_frota,
    afundados,
    posicao_valida,
    monta_tabuleiros
)

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

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

tabuleiro_jogador = posiciona_frota(frota)
tabuleiro_oponente = posiciona_frota(frota_oponente)

total_navios_oponente = 10
jogadas_feitas = []
jogando = True

while jogando:
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    linha_valida = False
    while linha_valida is False:
        linha = int(input("Jogador, qual linha deseja atacar? "))
        if 0 <= linha <= 9:
            linha_valida = True
        else:
            print("Linha inválida!")

    coluna_valida = False
    while coluna_valida is False:
        coluna = int(input("Jogador, qual coluna deseja atacar? "))
        if 0 <= coluna <= 9:
            coluna_valida = True
        else:
            print("Coluna inválida!")

    pos_repetida = [linha, coluna] in jogadas_feitas
    if pos_repetida:
        print("A posição linha " + str(linha) + " e coluna " + str(coluna) + " já foi informada anteriormente!")
    else:
        jogadas_feitas.append([linha, coluna])
        tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha, coluna)

        if afundados(frota_oponente, tabuleiro_oponente) == 10:
            print("Parabéns! Você derrubou todos os navios do seu oponente!")
            jogando = False









            




    




  
   

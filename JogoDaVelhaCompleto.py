def menu_entrada():
    '''
    Função inicial que mostra opções que o player pode escolher
    '''

    print(f"0. Sair\n" + "1. Jogar")
    opcao_ent = input()
    if opcao_ent == '0':
        return False
    else:
        return True

def escolha_player():
    '''
    Função apenas para escolha entre o 'o' e o 'x'
    '''

    print(f"\nPlayer 1, você é 'x' ou 'o'?")
    player1_opcao = input()
    if player1_opcao == 'o':
        player2_opcao = 'x'
    else:
        player2_opcao = 'o'

    print(f"\nPlayer 1: " + player1_opcao + "\nPlayer 2: " + player2_opcao)

    return(player1_opcao, player2_opcao)



def iniciar_tabuleiro():
    '''
    Inicia e reiniciar tabuleiro
    '''
    tabuleiro = [['0', '1', '2'],
                 ['3', '4', '5'],
                 ['6', '7', '8']]

    return tabuleiro


def imprimir_tabuleiro(tabuleiro):
    '''
    Imprime tabuleiro no console
    '''

    print("-----------")
    print('', tabuleiro[0][0], '|', tabuleiro[0][1], '|', tabuleiro[0][2])
    print('---+---+---')
    print('', tabuleiro[1][0], '|', tabuleiro[1][1], '|', tabuleiro[1][2])
    print('---+---+---')
    print('', tabuleiro[2][0], '|', tabuleiro[2][1], '|', tabuleiro[2][2])
    print("-----------")

def jogada_player(tabuleiro, player_opcao:str):
    """
    Faz a jogada selecionada pelo player
    """
    global coluna, linha

    marcado = False
    while not marcado:

        jogada = int(input("\nEscolha sua jogada:"))
        jogada_str = str(jogada)
        #jogada_str = str(jogada)
        #Atividade 1:
        #Defina a linha e a coluna  a partir da variavel jogada
        #voce pode usar o int para retornar
        #apenas a parte inteira do número
        linha = int(jogada/3)
        coluna = int(jogada%3)

        #Atividade 2: faça a marcação caso a posição não esteja marcada
        if tabuleiro[linha][coluna] == jogada_str:
            tabuleiro[linha][coluna] = player_opcao
            marcado = True
        else:
            print(f"Posição já marcada!")
                




def checagem_ganhador(tabuleiro, player_opcao):
    """
    Verifica se ha ganhador na rodada
    """
    global ganhador
    #Atividade 3: Substitua os "None" para checar se o jogador ganhou na LINHA
    #Dica: tabuleiro[0][1]==tabuleiro[1][2] and tabuleiro[1][2]==tabuleiro[2][2]
    #       é o mesmo que:  tabuleiro[0][1]==tabuleiro[1][2]==tabuleiro[2][2]

    for i in range(3):
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] == player_opcao:
            ganhador = player_opcao
            return ganhador

    #Atividade 4: Substitua os "None" para checar se o jogador ganhou na COLUNA
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == player_opcao:
            ganhador = player_opcao
            return ganhador

    #Atividade 5: Substitua os "None" para checar se o jogador ganhou na DIAGONAL
    #principal.
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == player_opcao:
        ganhador = player_opcao
        return ganhador

    #Atividade 5: Substitua os "None" para checar se o jogador ganhou na DIAGONAL
    #secundária
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == player_opcao:
        ganhador = player_opcao
        return ganhador

    return ganhador


def partida():
    contador_velha = 1
    global ganhador
    ganhador = 0

    player1_opcao, player2_opcao = escolha_player()

    tabuleiro = iniciar_tabuleiro()
    imprimir_tabuleiro(tabuleiro)


    while ganhador == 0:
        arr_player_opcao = [player1_opcao, player2_opcao]
        for player_opcao in arr_player_opcao:

            jogada_player(tabuleiro, player_opcao)
            imprimir_tabuleiro(tabuleiro)
            ganhador = checagem_ganhador(tabuleiro, player_opcao)
            contador_velha += 1
            if ganhador != 0:
                print(f"O player", player_opcao, "ganhou!\n")
                break
            if ganhador == 0 and contador_velha == 9:
                print(f"Deu velha !!!\n")
                ganhador = -1
                break


if __name__ == '__main__':
    while menu_entrada():
        partida()
    print("Fim do Jogo!")


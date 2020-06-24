from typing import List

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
    Função apenas para escolha entre o 'O' e o 'X'
    '''

    print(f"\nPlayer 1, você é X ou O?")
    player1_opcao = input()
    if player1_opcao == 'O':
        player2_opcao = 'X'
    else:
        player2_opcao = 'O'

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


def imprimir_tabuleiro(tabuleiro:List[List]):
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
        #Dica: vc pode criar uma variavel str para jogada!
        #Atividade 1:
        #Defina a linha e a coluna  a partir da variavel jogada
        #voce pode usar o int para retornar
        #apenas a parte inteira do número
        linha = None
        coluna = None

        #Atividade 2: faça a marcação caso a posição não esteja marcada
        #substitua os 'None'
        if tabuleiro[linha][coluna] != None:
            marcado = None
        else:
            print()



def checagem_ganhador(tabuleiro, player_opcao:str):
    """
    Verifica se ha ganhador na rodada
    """
    global ganhador

    #Atividade 3: Substitua os "None" para checar se o jogador ganhou na LINHA
    #Dica: tabuleiro[0][1]==tabuleiro[1][2] and tabuleiro[1][2]==tabuleiro[2][2]
    #       é o mesmo que:  tabuleiro[0][1]==tabuleiro[1][2]==tabuleiro[2][2]

    for i in None:
        if None:
            ganhador = player_opcao

    #Atividade 4: Substitua os "None" para checar se o jogador ganhou na COLUNA
    for i in None:
        if None:
            ganhador = player_opcao

    #Atividade 5: Substitua os "None" para checar se o jogador ganhou na DIAGONAL
    #PRINCIPAL
    if None:
        ganhador = player_opcao

    #Atividade 6: Substitua os "None" para checar se o jogador ganhou na DIAGONAL
    #SECUNDÁRIO
    if None:
        ganhador = player_opcao

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

            #Atividade 7: invoque os métodos jogada_player, imprimir tabuleiro e
            #checagem apropridadamente e substitua o None
            ganhador = None


            ####Fim do seu codigo :)###

            contador_velha += 1
            if ganhador != 0:
                print(f"O player", player_opcao, "ganhou!\n")
                break
            elif ganhador == 0 and contador_velha == 9:
                print(f"Deu velha !!!\n")
                ganhador = -1
                break


if __name__ == '__main__':
    #TABULEIRO PARA TESTES
    """
    tabuleiro = [['O', 'X', 'X'],
                 ['4', 'O', '6'],
                 ['7', '8', 'O']]
                 
    tabuleiro = [['O', 'X', 'X'],
                 ['4', 'o', 'X'],
                 ['7', '8', 'X']]
                 
    etc
    """

    #Teste de checagem
    #print(jogada_player(tabuleiro, player_opcao:str))

    #Teste de checagem
    #print(chegagem_ganhador(tabuleiro,"O"))
    #print(chegagem_ganhador(tabuleiro,"X"))


    #Código principal
    """
    while menu_entrada():
        partida()
    print("Fim do Jogo!")
    """

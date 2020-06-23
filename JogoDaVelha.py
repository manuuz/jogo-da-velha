
ganhador: int = 0

Player1opcao: str = ''
Player2opcao: str = ''
#TODO: Mudar nomenclatura menu_entrada
def MenuEntrada():
    print(f"0. Sair\n" + "1. Jogar")
    Opcao = input()
    if Opcao == '0':
        return False
    else:
        return True

def EscolhaPlayer():
    print(f"\nPlayer 1, você é X ou O?")
    Player1opcao = input()
    if Player1opcao == 'O':
        Player2opcao = 'X'
    else:
        Player2opcao = 'O'

    print(f"\nPlayer 1: " + Player1opcao + "\nPlayer 2: " + Player2opcao)

    return(Player1opcao, Player2opcao)



def IniciarTabuleiro():
    tabuleiro = [['1', '2', '3'],
                 ['4', '5', '6'],
                 ['7', '8', '9']]

    return tabuleiro


def ImprimirTabuleiro(tabuleiro:List[List]):
    print("-----------")
    print('', tabuleiro[0][0], '|', tabuleiro[0][1], '|', tabuleiro[0][2])
    print('---+---+---')
    print('', tabuleiro[1][0], '|', tabuleiro[1][1], '|', tabuleiro[1][2])
    print('---+---+---')
    print('', tabuleiro[2][0], '|', tabuleiro[2][1], '|', tabuleiro[2][2])
    print("-----------")

def JogadaPlayer(tabuleiro, player_opcao:str):
    """
    Solicita ao
    """
    marcou = False
    while not marcou:

        jogada = int(input("\nEscolha sua jogada:"))

        #Atividade 1:
        #Defina a linha e a coluna  a partir da variavel jogada
        #voce pode usar o int para retornar
        #apenas a parte inteira do número
        linha = int(jogada/3)-1
        coluna = (jogada-1)%3

        #Atividade 2: faça a marcação caso a posição não esteja marcada
        if tabuleiro[linha][coluna] != "":
            marcou = True
            tabuleiro[linha][coluna] = player_opcao
        else:
            print("Posição já marcada!")
    return linha,coluna



def Checagem(tabuleiro, player_opcao):
    """
    Verifica se ha ganhador na rodada
    """
    #Atividade 3: Substitua os "None" para checar se o jogador ganhou na LINHA
    #Dica: tabuleiro[0][1]==tabuleiro[1][2] and tabuleiro[1][2]==tabuleiro[2][2]
    #       é o mesmo que:  tabuleiro[0][1]==tabuleiro[1][2]==tabuleiro[2][2]
    for i in None:
        if None:
            ganhador = player_opcao

    #Atividade 4: Substitua os "None" para checar se o jogador ganhou na COLUNA
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == player_opcao:
            ganhador = player_opcao

    #Atividade 5: Substitua os "None" para checar se o jogador ganhou na DIAGONAL
    #principal.
    if None:
        ganhador = player_opcao
    #Atividade 5: Substitua os "None" para checar se o jogador ganhou na DIAGONAL
    #secundária
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == player_opcao:
        ganhador = player_opcao

    return ganhador


def Partida():
    contador_velha = 1

    Player1opcao, Player2opcao = EscolhaPlayer()

    tabuleiro = IniciarTabuleiro()
    ImprimirTabuleiro(tabuleiro)
    ganhador = 0
    while ganhador == 0:
        arr_player_opcao = [Player1opcao,Player2opcao]

        for player_opcao in arr_player_opcao:
            #Atividade 6: invoque os métodos jogada_player, imprimir tabuleiro e
            #checagem apropridadamente
            JogadaPlayer(tabuleiro, player_opcao)
            ImprimirTabuleiro(tabuleiro)
            ganhador = Checagem(tabuleiro, player_opcao)


            ####Fim do seu codigo :)###
            contador_velha += 1
            if ganhador != 0:
                print(f"O player", ganhador, "ganhou!\n")
                break
            elif ganhador == 0 and contador_velha == 9:
                print(f"Deu velha !!!\n")
                break


if __name__ == '__main__':
    #TABULEIRO PARA TESTES
    """
    tabuleiro = [['o', '2', '3'],
                 ['4', 'o', '6'],
                 ['7', '8', 'x']]
    """



    #Teste de checagem
    #print(JogadaPlayer(tabuleiro, player_opcao:str))

    #Teste de checagem
    """
    print(Checagem(tabuleiro,"o"))
    print(Checagem(tabuleiro,"x"))
    """

    #Código principal
    """
    while MenuEntrada():
        Partida()
    print("Fim do Jogo!")
    """

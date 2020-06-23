
ganhador: int = 0

Player1opcao: str = ''
Player2opcao: str = ''

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


def ImprimirTabuleiro(tabuleiro):
    print("-----------")
    print('', tabuleiro[0][0], '|', tabuleiro[0][1], '|', tabuleiro[0][2])
    print('---+---+---')
    print('', tabuleiro[1][0], '|', tabuleiro[1][1], '|', tabuleiro[1][2])
    print('---+---+---')
    print('', tabuleiro[2][0], '|', tabuleiro[2][1], '|', tabuleiro[2][2])
    print("-----------")

def JogadaPlayer(tabuleiro, PlayerOpcao):
    Jogada = int(input("\nEscolha sua jogada:"))

    if Jogada == 1 and tabuleiro[0][0] == '1':
        tabuleiro[0][0] = PlayerOpcao

    elif Jogada == 2 and tabuleiro[0][1] == '2':
        tabuleiro[0][1] = PlayerOpcao

    elif Jogada == 3 and tabuleiro[0][2] == '3':
        tabuleiro[0][2] = PlayerOpcao

    elif Jogada == 4 and tabuleiro[1][0] == '4':
        tabuleiro[1][0] = PlayerOpcao

    elif Jogada == 5 and tabuleiro[1][1] == '5':
        tabuleiro[1][1] = PlayerOpcao

    elif Jogada == 6 and tabuleiro[1][2] == '6':
        tabuleiro[1][2] = PlayerOpcao

    elif Jogada == 7 and tabuleiro[2][0] == '7':
        tabuleiro[2][0] = PlayerOpcao

    elif Jogada == 8 and tabuleiro[2][1] == '8':
        tabuleiro[2][1] = PlayerOpcao

    elif Jogada == 9 and tabuleiro[2][2] == '9':
        tabuleiro[2][2] = PlayerOpcao


def Checagem(tabuleiro, Player1opcao, Player2opcao):

    # COLUNAS
    global ganhador
    for i in range(3):
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] == Player1opcao:
            ganhador = 1
        elif tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] == Player2opcao:
            ganhador = 2

    # LINHAS
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == Player1opcao:
            ganhador = 1
        elif tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == Player2opcao:
            ganhador = 2

    # DIAGONAIS
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == Player1opcao:
        ganhador = 1
    elif tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == Player2opcao:
        ganhador = 2

    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == Player1opcao:
        ganhador = 1
    elif tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == Player2opcao:
        ganhador = 2

    return ganhador


def Partida():
    contador_velha = 1

    Player1opcao, Player2opcao = EscolhaPlayer()

    tabuleiro = IniciarTabuleiro()
    ImprimirTabuleiro(tabuleiro)

    while ganhador == 0:
        JogadaPlayer(tabuleiro, Player1opcao)
        ImprimirTabuleiro(tabuleiro)
        Checagem(tabuleiro, Player1opcao, Player2opcao)
        if ganhador != 0:
            print(f"O player", ganhador, "ganhou!\n")
            break

        JogadaPlayer(tabuleiro, Player2opcao)
        ImprimirTabuleiro(tabuleiro)
        Checagem(tabuleiro, Player1opcao, Player2opcao)
        contador_velha += 1
        if ganhador != 0:
            print(f"O player", ganhador, "ganhou!\n")
            break
        elif ganhador == 0 and contador_velha == 6:
            print(f"Deu velha !!!\n")
            break


if __name__ == '__main__':
    while MenuEntrada():
        Partida()
    print("Fim do Jogo!")

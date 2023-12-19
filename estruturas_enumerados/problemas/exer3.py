# Analise:
#
#   Determinar o nivel atual do jogador e a quantidade de horas jogadas em uma semana e calcular o nivel
# atual do jogador.
#
# tempo_jogado_semanalmente for entre 4h a 5h , permanece no mesmo nível.
# tempo_jogado_semanalmente for < 4h , -1 nivel a cada 1 hora que faltou para alcancar as 4hs.
# tempo_jogado_semanalmente > 5h , +1 nivel a cada hora jogada além das 5hs.

# Definição:
#
#   O nivel atual e a quantidade de horas serao representados por valores positivos.
#   A quantidade maxima semanalmente é até 7 niveis.


from dataclasses import dataclass

@dataclass
class Jogador:
    NIVEL_ATUAL : int
    TEMPO_JOGO : float

def nivel_atual_jogador(Player:Jogador) -> int:
    '''
        Calcular o *nivel atual* do jogador atraves da quantidade horas jogadas em uma semana.

        Se o 4hs <= *tempoJ* <= 5hs  . O jogador permanece no mesmo nivel.
        Se o *tempoJ* < 4hs . O jogador perde 1 nivel a cada 1h que faltou para alcancar as 4hs
        Se o *tmpoJ* > 5hs .  O jogador aumentam 1 nivel para cada hora jogada alem das 5hs.

        O limite de niveis  recebidos por semana devem ser ate 7 niveis.

        O nivel do jogador nao pode < 0.

    Exemplos
    >>> nivel_atual_jogador(Jogador(0,6))
    1
    >>> nivel_atual_jogador(Jogador(4,8))
    7
    >>> nivel_atual_jogador(Jogador(5,3))
    4
    >>> nivel_atual_jogador(Jogador(2,4))
    2
    >>> nivel_atual_jogador(Jogador(0,2))
    0
    >>> nivel_atual_jogador(Jogador(24,7))
    25
    '''

    if Player.TEMPO_JOGO < 4:
        Player.NIVEL_ATUAL = Player.NIVEL_ATUAL - (4 - Player.TEMPO_JOGO)
    elif Player.TEMPO_JOGO > 5:
        Player.NIVEL_ATUAL += (Player.TEMPO_JOGO - 5)
        
    if Player.NIVEL_ATUAL > 25:
        Player.NIVEL_ATUAL = 25
    elif Player.NIVEL_ATUAL < 0:
        Player.NIVEL_ATUAL = 0
    
    return Player.NIVEL_ATUAL




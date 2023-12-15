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

def jogador(nivelA:int, tempoJ:float) -> Jogador:
    '''
        Calcular o *nivel atual* do jogador atraves da quantidade horas jogadas em uma semana.

        Se o 4hs <= *tempoJ* <= 5hs  . O jogador permanece no mesmo nivel.
        Se o *tempoJ* < 4hs . O jogador perde 1 nivel a cada 1h que faltou para alcancar as 4hs
        
    '''


    





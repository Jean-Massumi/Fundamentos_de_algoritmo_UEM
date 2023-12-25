# Análise:
#   Determine quantas casas de um tabuleiro um personagem pode andar dependendo da posição que está e
#   da direção que ele está.

# Definição:
#   As linhas e colunas  do tabuleiro são enumeradas de 1 a 10
#   O personagem não pode sair do tabuleiro.
#   A posicao(linhas e  colunas) do personagem serão representados por valores inteiros e a sua direção
#   por uma string.

from dataclasses import dataclass

@dataclass
class Personagem:
    POSICAO_LINHA : int
    POSICAO_COLUNA : int
    DIRECAO : str

def avancar_direcao(p:Personagem) -> str:
    '''
        Determinar quantas casas maximas um personagem pode avancar depende direção que ele está virado.

    Exemplos:
    >>> avancar_direcao(Personagem(3, 7, 'Oeste'))
    'O personagem pode andar 6 casas para o Oeste'
    >>> avancar_direcao(Personagem(9, 2, 'Sul'))
    'O personagem pode andar 8 casas para o Sul'
    >>> avancar_direcao(Personagem(4, 1, 'Leste'))
    'O personagem pode andar 9 casas para o Leste'
    >>> avancar_direcao(Personagem(5, 8, 'Norte'))
    'O personagem pode andar 5 casas para o Norte'

    '''

    if p.DIRECAO == 'Norte':
        passos = f'O personagem pode andar {10-p.POSICAO_LINHA} casas para o Norte'
    elif p.DIRECAO == 'Sul':
        passos = f'O personagem pode andar {p.POSICAO_LINHA - 1} casas para o Sul'
    elif p.DIRECAO == 'Leste':
        passos = f'O personagem pode andar {10-p.POSICAO_COLUNA} casas para o Leste'
    else:
        passos = f'O personagem pode andar {p.POSICAO_COLUNA - 1} casas para o Oeste'

    return passos
















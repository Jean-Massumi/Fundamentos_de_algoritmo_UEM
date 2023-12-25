# Análise:
#   Determinar quantas casas de um tabuleiro um personagem pode andar dependendo da posição que está e
#   da direção que ele está.

# Definição:
#   As linhas e colunas  do tabuleiro são enumeradas de 1 a 10
#   O personagem não pode sair do tabuleiro.
#   A posicao(linhas e  colunas) do personagem serão representados por valores inteiros e a sua direção
#   por uma string.

from dataclasses import dataclass
from enum import Enum,auto

class Direcao(Enum):
    NORTE = auto()
    SUL = auto()
    LESTE = auto()
    OESTE = auto()

@dataclass
class Personagem:
    POSICAO_LINHA : int
    POSICAO_COLUNA : int
    DIRECAO : Direcao

# def avancar_direcao(p:Personagem) ->int:






















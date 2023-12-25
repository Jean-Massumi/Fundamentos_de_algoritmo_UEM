# Análise:
#   Determinar o melhor candidato classificado em uma prova de 0 a 100, caso haja empate , o candidato com menor 
#   inscrição é classificado primeiro.

# Definição:
#   Os pontos da prova e a inscrição do candidato serão representados por valores inteiros.

from dataclasses import dataclass

@dataclass
class Candidato_1:
    INSCRICAO : int
    PONTOS : int

@dataclass
class Candidato_2:
    INSCRICAO : int
    PONTOS : int

def classificacao(c1:Candidato_1, c2:Candidato_2) -> str:
    '''
        Determinar atraves da inscricao e da pontuacao , qual dos dois candidatos , melhor se classificou.

    Exemplos
    >>> classificacao(Candidato_1(32, 89), Candidato_2(23, 89))
    'O melhor classificado foi o candidato 2'
    >>> classificacao(Candidato_1(15, 89), Candidato_2(31, 89))
    'O melhor classificado foi o candidato 1'
    >>> classificacao(Candidato_1(67, 46), Candidato_2(44, 63))
    'O melhor classificado foi o candidato 2'
    >>> classificacao(Candidato_1(2, 58), Candidato_2(11, 21))
    'O melhor classificado foi o candidato 1'
    '''

    if c1.PONTOS == c2.PONTOS:
        if c1.INSCRICAO < c2.INSCRICAO:
            melhor_classificado = 'O melhor classificado foi o candidato 1'
        else:
            melhor_classificado = 'O melhor classificado foi o candidato 2'
    elif c1.PONTOS < c2.PONTOS:
        melhor_classificado = 'O melhor classificado foi o candidato 2'
    else:
        melhor_classificado = 'O melhor classificado foi o candidato 1'

    return melhor_classificado

















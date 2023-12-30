# Análise:
#   Desempenho do time:
#   - Pontos (3 por vitória e 1 por empate)
#   - Vitórias 
#   - Saldo (Diferença entre gols marcados e gols sofridos)
#
#   Calcular o desempenho de um time a partir dos resultados das partidas que ele jogou.

from dataclasses import dataclass

@dataclass
class Desempenho:
    '''
        Um time e seu desempenho em um campeonato
    '''
    TIME : str
    PONTOS : int
    VITÓRIAS : int
    SALDO : int

@dataclass
class Resultado:
    '''
        Resultado de uma partida de um campeonato
    '''
    GOLS_MARCADOS : int
    GOLS_SOFRIDOS : int

def calcula_desempenho(time:str, jogos:list[Resultado] ):
    '''
        Calcula o desempenho do *time* considerando os *resultados* dos seu jogos.

    Exemplos:
    >>> calcula_desempenho('Santos', [])
    Desempenho(TIME='Santos', PONTOS=0, VITÓRIAS=0, SALDO=0)
    >>> calcula_desempenho('Sao Paulo', [Resultado(2, 1), Resultado(2, 4), Resultado(0, 0)])
    Desempenho(TIME='Sao Paulo', PONTOS=4, VITÓRIAS=1, SALDO=-1)
    
    '''

    d = Desempenho(time, 0, 0, 0)
    for resultado in jogos:
        d = atualiza_desempenho(d, resultado.GOLS_MARCADOS, resultado.GOLS_SOFRIDOS)

    return d


def atualiza_desempenho(d:Desempenho, GM:int, GF:int):
    '''
        Devolve um novo desempenho atualizado a partir de *d* considerando que o
        time fez *GM* gols e o adversário *GF* gols.

        GM : Gols Marcados
        GF : Gols Sofridos

        Se o time ganhou, +3 pontos e +1 vitória.
        Se o time empatou, +1 ponto.

        O saldo de gols é obtido GM - GF, onde os gols nao pode ser negativos.


    >>> atualiza_desempenho(Desempenho('Guairaca', 6, 2, 3), 1, 0)
    Desempenho(TIME='Guairaca', PONTOS=9, VITÓRIAS=3, SALDO=4)
    >>> atualiza_desempenho(Desempenho('Curitiba', 3, 1, 2), 2, 2)
    Desempenho(TIME='Curitiba', PONTOS=4, VITÓRIAS=1, SALDO=2)
    >>> atualiza_desempenho(Desempenho('Alto Paraná', 2, 0, 3), 1, 4)
    Desempenho(TIME='Alto Paraná', PONTOS=2, VITÓRIAS=0, SALDO=0)
    '''

    pontos = d.PONTOS
    vitorias = d.VITÓRIAS
    saldo = d.SALDO + GM - GF

    if GM > GF:
        pontos += 3
        vitorias += 1
    elif GM == GF:
        pontos += 1

    return Desempenho(d.TIME, pontos, vitorias, saldo)


















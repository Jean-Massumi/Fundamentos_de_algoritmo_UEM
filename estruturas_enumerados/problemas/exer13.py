# Análise:
#   O desempenho de um time de futebol em um determinado campeonato é dado pelo número de pontos, número de 
#   vitórias e saldos de gols.
#   1 - Determine qual de dois time ,teve um melhor desempenho.
#   2 - Atualize o desempenho de um time dado um resultado de um jogo.

# Definição:
#   Cada jogo ganho pelo time dá 3 pontos e empate 1 ponto.
#   O saldo de gols é a diferença entre gols marcados e sofridos.
#   Os pontos e os números de vitórias de um time serão representados por valores inteiros positivos.
#   O saldo de gols será representado por valores inteiros .

from dataclasses import dataclass

@dataclass
class Time:
    NOME : str
    PONTOS : int
    VITÓRIAS : int
    SALDOS_GOLS: int

def melhor_desempenho(T1:Time , T2:Time) -> str:
    '''
        Determinar qual dos dois times teve o melhor desempenho , mediante aos critérios de pontos, vitórias e
        saldos de gols.
        Caso haja empate a ordem alfatica dos nomes é usada para desempate.
    
    Exemplos:
    >>> melhor_desempenho(Time('Vasco', 39, 11, 19), Time('Santos', 39, 11, 19)) # Caso de empate
    'Santos teve o melhor desempenho!'      # O desempate é feito por ordem alfabetica e como *S* vem antes do
                                            # *T* o Santos teve o melhor desempenho.
    >>> melhor_desempenho(Time('Palmeiras', 43, 14, 22), Time('Curitiba', 27, 9, 17))
    'Palmeiras teve o melhor desempenho!'
    >>> melhor_desempenho(Time('Flamengo', 11, 3, 6), Time('São Paulo', 15, 5, 5))
    'São Paulo teve o melhor desempenho!'
    '''





















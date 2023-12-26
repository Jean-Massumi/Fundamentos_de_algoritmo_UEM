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
    >>> melhor_desempenho(Time('Vasco', 39, 11, 19), Time('Santos', 39, 11, 19)) 
    'Santos teve o melhor desempenho!'
    >>> melhor_desempenho(Time('Atletico-MG', 54, 17, 33), Time('Atletico-GO', 54, 17, 33)) 
    'Atletico-GO teve o melhor desempenho!'
    >>> melhor_desempenho(Time('Palmeiras', 43, 14, 22), Time('Curitiba', 27, 9, 17))
    'Palmeiras teve o melhor desempenho!'
    >>> melhor_desempenho(Time('Flamengo', 11, 3, 6), Time('São Paulo', 15, 5, 5))
    'São Paulo teve o melhor desempenho!'
    '''

    if T1.PONTOS > T2.PONTOS:
        time_com_desempenho = f'{T1.NOME} teve o melhor desempenho!'
    elif T1.PONTOS < T2.PONTOS:
        time_com_desempenho = f'{T2.NOME} teve o melhor desempenho!'
    elif (T1.PONTOS == T2.PONTOS) and (T1.VITÓRIAS == T2.VITÓRIAS) and (T1.SALDOS_GOLS == T2.SALDOS_GOLS):
        for i in range(len(T1.NOME)):
            if T1.NOME[i] != T2.NOME[i]:
                if T1.NOME[i] < T2.NOME[i]:
                    time_com_desempenho = f'{T1.NOME} teve o melhor desempenho!'
                else:
                    time_com_desempenho = f'{T2.NOME} teve o melhor desempenho!'
                break

    return time_com_desempenho


@dataclass
class Time_Partida:
    '''
        Situação da ultima partida jogada de um time.
    '''
    SITUACAO : str
    GOLS_MARCADOS : int
    GOLS_SOFRIDOS : int

def atualiza_desempenho(T1:Time,T1P:Time_Partida, T2:Time , T2P:Time_Partida) -> str:
    '''
        Atualiza o desempenho de um time conforme o resultado de um jogo.
    
    >>> atualiza_desempenho(Time('Vasco', 39, 11, 19), Time_Partida('Vitória', 3, 1), \
                            Time('Santos', 39, 11, 19), Time_Partida('Derrota', 1, 3))
    'Time:Vasco ,Pontos:42 ,Vitórias:12 ,Saldos de gols:21\
     Time:Santos ,Pontos:39 ,Vitórias:11 ,Saldos de gols:17'

    >>> atualiza_desempenho(Time('Flamengo', 11, 3, 6), Time_Partida('Derrota', 2, 5), \
                            Time('São Paulo', 15, 5, 5), Time_Partida('Vitória', 5, 2))
    'Time:Flamengo ,Pontos:11 ,Vitórias:3 ,Saldos de gols:3\
     Time:São Paulo ,Pontos:18 ,Vitórias:6 ,Saldos de gols:8'

    '''
    if T1P.SITUACAO == 'Vitória':
        T1.PONTOS += 3
        T1.VITÓRIAS += 1
        T1.SALDOS_GOLS += T1P.GOLS_MARCADOS - T1P.GOLS_SOFRIDOS
    else:
        T1.SALDOS_GOLS += T1P.GOLS_MARCADOS - T1P.GOLS_SOFRIDOS

    if T2P.SITUACAO == 'Vitória':
        T2.PONTOS += 3
        T2.VITÓRIAS += 1
        T2.SALDOS_GOLS += T2P.GOLS_MARCADOS - T2P.GOLS_SOFRIDOS
    else:
        T2.SALDOS_GOLS += T2P.GOLS_MARCADOS - T2P.GOLS_SOFRIDOS

    return f'Time:{T1.NOME} ,Pontos:{T1.PONTOS} ,Vitórias:{T1.VITÓRIAS} ,Saldos de gols:{T1.SALDOS_GOLS}\
     Time:{T2.NOME} ,Pontos:{T2.PONTOS} ,Vitórias:{T2.VITÓRIAS} ,Saldos de gols:{T2.SALDOS_GOLS}'


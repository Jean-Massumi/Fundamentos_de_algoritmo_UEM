# Análise:
#   Determinar qual foi o resultado de uma eleicao.
#   Se o primeiro candidato tiver mais votos que o segundo, entao o primeiro candidato foi eleito
#   Caso contrario o segundo candidato foi eleito.
#   Se os votos brancos foram mais que 50% dos votos totais, uma nova eleicao deve ser convocada.

# Denifição: 
#   Como na eleição temos tres tipos de votos e votos totais, ela será representada por uma estrutura.

from dataclasses import dataclass

@dataclass
class Eleicao:
    '''
        Representa a quantidade de cada voto feito na eleição.
    '''
    VOTO1 : int
    VOTO2 : int
    VOTO_BRANCO : int  

def resultado_eleicao(total_votos:list) -> str:
    '''
        Determinar qual será o resultado da eleicao.

        Se voto branco for > 50% do total de votos , entao uma nova eleicao deve ser convocada.
        Se voto1 == voto2 , entao uma nova eleição deve ser convocada.
        Se voto1 > voto2, entao o Candidato 1 foi eleito.
        Se voto2 > voto1, entao o Candidato 2 foi eleito.

    Exemplos:
    >>> resultado_eleicao([1, 2, 0, 1, 0, 1, 1, 2, 0])
    'Candidato 1 eleito!'
    >>> resultado_eleicao([1, 2, 0, 1, 0, 1, 1, 2, 0, 0, 0, 0, 0, 0])
    'Uma nova eleição deve ser convocada!'
    >>> resultado_eleicao([2, 2, 0, 1, 2, 2, 1, 2, 0])
    'Candidato 2 eleito!'
    '''

    e = Eleicao(0, 0, 0)

    e = contar_voto(e, total_votos)

    if e.VOTO_BRANCO > len(total_votos) * 0.5:
        resultado = 'Uma nova eleição deve ser convocada!'
    elif e.VOTO1 == e.VOTO2:
        resultado = 'Uma nova eleição deve ser convocada!'
    elif e.VOTO1 > e.VOTO2:
        resultado = 'Candidato 1 eleito!'
    else:
        resultado = 'Candidato 2 eleito!'

    return resultado



def contar_voto(e:Eleicao, total_v:list) -> Eleicao:
    '''
        Conta os votos de cada voto especificado e devolve para *resultado_eleicao*
    
    Exemplos:
    >>> contar_voto(Eleicao(0, 0, 0), [1, 1, 1, 0, 2, 0])
    Eleicao(VOTO1=3, VOTO2=1, VOTO_BRANCO=2)
    >>> contar_voto(Eleicao(0, 0, 0), [2, 0, 1, 1, 0, 2, 2])
    Eleicao(VOTO1=2, VOTO2=3, VOTO_BRANCO=2)
    >>> contar_voto(Eleicao(0, 0, 0), [0, 2, 0, 2, 0, 1, 0, 0, 0, 2, 0, 2])
    Eleicao(VOTO1=1, VOTO2=4, VOTO_BRANCO=7)
    >>> contar_voto(Eleicao(0, 0, 0), [0, 2, 1, 1, 2, 1, 2])
    Eleicao(VOTO1=3, VOTO2=3, VOTO_BRANCO=1)
    '''

    voto1 = e.VOTO1
    voto2 = e.VOTO2
    branco = e.VOTO_BRANCO

    for voto in total_v:
        if voto == 1:
            voto1 += 1
        elif voto == 2:
            voto2 += 1
        else:
            branco += 1

    return Eleicao(voto1, voto2, branco)























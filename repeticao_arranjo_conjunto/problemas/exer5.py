# Análise:
#   Se 2/3 das notas finais das disciplinas for maiores de 9.0 , o aluno recebe a homenagem.
#
#   Determinar se o aluno receberá a homenagem (Lauréa Academica).

from dataclasses import dataclass

@dataclass
class Disciplina:
    '''
        Representa a nota final da disciplina.   
    '''
    NOTA : float

def homenagem(Notas:list[Disciplina]) -> bool:
    '''
        Devolve *True* se 2/3 das notas finais de um aluno foram maiores que 9.0. 
        Devolve *False* caso contraio
    
    Exemplos:
    >>> homenagem([Disciplina(9.2), Disciplina(6.0), Disciplina(9.3)])
    True
    >>> homenagem([Disciplina(7.0), Disciplina(6.5), Disciplina(9.2)])
    False
    >>> homenagem([Disciplina(9.1), Disciplina(9.1), Disciplina(9.1)])
    True

    '''

    qtd_notas = len(Notas) * 2 / 3
    notas_acima_90 = 0

    for nota in Notas:
        if nota.NOTA > 9.0 :
            notas_acima_90 += 1

    return notas_acima_90 >= qtd_notas

























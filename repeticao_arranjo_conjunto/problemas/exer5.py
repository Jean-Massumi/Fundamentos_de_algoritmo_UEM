# Análise:
#   Se 2/3 das notas finais das disciplinas for maiores de 9.0 , o aluno recebe a homenagem.
#
#   Determinar se o aluno receberá a homenagem (Lauréa Academica).

from dataclasses import dataclass

@dataclass
class Diciplina:
    '''
        Representa a nota final da disciplina.   
    '''
    NOTA : float

def homenagem(Notas:list[Diciplina]) -> bool:
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
























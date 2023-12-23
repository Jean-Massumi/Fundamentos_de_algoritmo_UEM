# Análise:
#   Determinar a média final das 4 avaliações e a situação do aluno. 

# Definição:
#   As notas serão representadas por valores float de 0 a 10.
#   A situação do aluno pode ser representado por:
#       Aprovado ,média final >= a 7.
#       Reprovado ,média final < 4.
#       Exame , 4 <= média final < 7.

from dataclasses import dataclass
from enum import Enum,auto

class Situacao(Enum):
    '''
        Enumerados do tipo de *Situacao* que irá representar qual será a situação do aluno , dependendo 
        da média final.
    '''
    APROVADO = auto()
    REPROVADO = auto()
    EXAME = auto()

@dataclass
class Aluno:
    '''
        Estrutura do tipo *Aluno* que tem 4 notas.
    '''
    n1 : float
    n2 : float
    n3 : float
    n4 : float

def situação_média(avaliações:Aluno) -> str:
    '''
        Calcular a média final das 4 avaliações e devolver a situação do aluno.
    
    Se a média final for >= 7 , aprovado.
    Se a média final for < 4 , reprovado.
    Se a 4 <= média final < 7 , exame.

    Exemplos:
    >>> situação_média(Aluno(7.0, 7.0, 7.0, 7.0)).name
    'APROVADO'
    >>> situação_média(Aluno(8.3, 6.1, 9.4, 6.9)).name
    'APROVADO'
    >>> situação_média(Aluno(4.0, 4.0, 4.0, 4.0)).name
    'EXAME'
    >>> situação_média(Aluno(3.3, 7.1, 5.5, 6.7)).name
    'EXAME'
    >>> situação_média(Aluno(3.9, 3.9, 3.9, 3.9)).name
    'REPROVADO'
    >>> situação_média(Aluno(0.4, 3.7, 8.1, 2.4)).name
    'REPROVADO'
    '''

    média:float = (avaliações.n1 + avaliações.n2 + avaliações.n3 + avaliações.n4) / 4

    if média >= 7:
        situacao = Situacao.APROVADO
    elif média < 4:
        situacao = Situacao.REPROVADO
    else:
        situacao = Situacao.EXAME

    return situacao


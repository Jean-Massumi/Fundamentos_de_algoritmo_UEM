# Análise:
#   Determinar o retangulo Delimitador de menor altura e menor largura que pode cobrir um conjunto de pontos
#   em um plano cartesiano.

# Definição:
#   Os lados do retangulo deve ser paralelos aos eixos x e y.
#   Como o retangulo Delimitador devera possuir 4 pontos distintos ,entao sera representado por uma estrutura.

from dataclasses import dataclass

@dataclass
class Retangulo:
    '''
        Representa os pontos do menor retangulo delimitador em um plano cartesino.
    '''
    PONTO_1 : tuple
    PONTO_2 : tuple
    PONTO_3 : tuple
    PONTO_4 : tuple

        
def retangulo_delimitador(conjunto_pontos:list):
    '''
        Determinar o menor retangulo dilimitador ,dado um conjunto de pontos em um plano cartesiano
    
    Exemplos:
    >>> retangulo_delimitador([(4,2)])
    Retangulo(PONTO_1=(5,3), PONTO_2=(3,3), PONTO_3=(5,1), PONTO_4=(3,1))
    '''

    x_max = x_min = y_max = y_min = 0

    













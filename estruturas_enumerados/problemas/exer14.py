# Análise:
#   Determine se o clique do mouse aconteceu sobre a janela e verifique se os espaços de duas janelas 
#   sobrepõem>

# Difinição:
#   Os pixels sao organizados por linhas e colunas e serao representados por valores inteiros positivos A x B.

from dataclasses import dataclass

@dataclass
class Janela:
    '''
        Quantidade de linhas e colunas de uma janela.
    '''
    LINHAS : int
    COLUNAS : int 

@dataclass
class Mouse:
    '''
        Local da linha e coluna onde o ocorreu o clique do mouse.
    '''
    LINHAS : int
    COLUNAS : int

def verificar_clique(j:Janela, m:Mouse) ->str:
    '''
        Verificar se o clique do mouse ocorreu sobre a janela.

    Exemplos:
    >>> verificar_clique(Janela(720, 580), Mouse(590, 310))
    'O clique aconteceu sobre a janela'
    >>> verificar_clique(Janela(240, 110), Mouse(240, 110))
    'O clique aconteceu sobre a janela'
    >>> verificar_clique(Janela(670, 390), Mouse(810, 310))
    'O clique aconteceu fora da janela'
    >>> verificar_clique(Janela(1024, 720), Mouse(810, 980))
    'O clique aconteceu fora da janela'
    >>> verificar_clique(Janela(420, 420), Mouse(760, 815))
    'O clique aconteceu fora da janela'
    '''

    if m.LINHAS <= j.LINHAS and m.COLUNAS <= j.COLUNAS:
        resp = 'O clique aconteceu sobre a janela'
    else:
        resp = 'O clique aconteceu fora da janela'

    return resp
















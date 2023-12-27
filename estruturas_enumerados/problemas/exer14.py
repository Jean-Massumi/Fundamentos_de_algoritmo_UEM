# Análise:
#   Determine se o clique do mouse aconteceu sobre a janela e verifique se os espaços de duas janelas 
#   sobrepõem>

# Difinição:
#   Os pixels sao organizados por linhas e colunas e serao representados por valores inteiros positivos A x B.

from dataclasses import dataclass
from os import system

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


def entrada():
    system('cls')
    '''
        Receber as informacoes da janela e do mouse e passar como paramentros para funcao *verificar_clique*
        , e devolve monstrando se o clique ocorreu sobre a janela ou nao.
        '''
    print('Dimensões dos pixels de uma janela de um monitor!')
    l1 : int = input('Linhas: ') 
    c1 : int = input('Colunas: ')
    print()
    print('Dimensões de onde ocorreu o clique do mouse!')
    l2 : int = input('Linhas: ')
    c2 : int = input('Colunas: ')

    verificacao = verificar_clique(Janela(l1, c1), Mouse(l2, c2))

    return verificacao


print(entrada())


def janela_sobrepoe(j1:Janela, j2:Janela) -> str:
    '''
        Verificar se os espaços de duas janelas se sobrepõem

    Exemplos:
    >>> janela_sobrepoe(Janela(720, 810), Janela(720, 810))
    'As janelas não se sobrepõem'
    >>> janela_sobrepoe(Janela(1280, 880), Janela(410, 320))
    'Uma das janelas se sobrepõem a outra'
    >>> janela_sobrepoe(Janela(560, 610), Janela(1890, 990))
    'Uma das janelas se sobrepõem a outra'

    '''

    if j1.LINHAS == j2.LINHAS and j1.COLUNAS == j2.COLUNAS:
        resp = 'As janelas não se sobrepõem'
    elif (j1.LINHAS < j2.LINHAS and j1.COLUNAS < j2.COLUNAS) or (j2.LINHAS < j1.LINHAS and j2.COLUNAS < j1.COLUNAS):
            resp = 'Uma das janelas se sobrepõem a outra'
        
    return resp














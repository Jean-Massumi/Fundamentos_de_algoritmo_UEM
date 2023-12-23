# Análise:
#   Determinar a partir do nome e simbolo de dois jogadores, quem irá ganhar o jokenpô.

# Definição:
#   A decisão para saber quem ganhou é feita da seguinte forma:
#       Pedra ganha de tesoura.
#       Tesoura ganha do papel.
#       Papel ganha da pedra.

from dataclasses import dataclass

@dataclass
class Jogador1:
    NOME : str
    SÍMBOLO : str

@dataclass
class Jogador2:
    NOME : str
    SÍMBOLO : str

def jogo_jokenpo(player1:Jogador1, player2:Jogador2) -> str:
    '''
        Determinar a partir do nome e simbolo, qual dos jogadores irá ganhar no jokenpô.

        O jogo funciona da seguinte forma:
            Pedra ganha da tesoura.
            Tesoura ganha do papel.
            Papel ganha da pedra.
        Caso os dois jogadores jogarem o mesmo simbolo, então será empate.


    Exemplos:
    >>> jogo_jokenpo(Jogador1('Lucas','Pedra'), Jogador2('Oscar', 'Tesoura'))
    'Lucas ganhou'
    >>> jogo_jokenpo(Jogador1('Joao','Tesoura'), Jogador2('Ana', 'Papel'))
    'Joao ganhou'
    >>> jogo_jokenpo(Jogador1('Beatriz','Papel'), Jogador2('Paulo', 'Pedra'))
    'Beatriz ganhou'
    >>> jogo_jokenpo(Jogador1('Marcelo','Tesoura'), Jogador2('Carol', 'Tesoura'))
    'Empate'
    >>> jogo_jokenpo(Jogador1('Rafael','Papel'), Jogador2('Bruna', 'Tesoura'))
    'Bruna ganhou'
    '''

    if player1.SÍMBOLO == player2.SÍMBOLO:
        resultado = 'Empate'
    elif player1.SÍMBOLO == 'Pedra':
        if player2.SÍMBOLO == 'Tesoura':
            resultado = f'{player1.NOME} ganhou'
        elif player2.SÍMBOLO == 'Papel':
            resultado = f'{player2.NOME} ganhou'
    elif player1.SÍMBOLO == 'Tesoura':
        if player2.SÍMBOLO == 'Papel':
            resultado = f'{player1.NOME} ganhou'
        elif player2.SÍMBOLO == 'Pedra':
            resultado = f'{player2.NOME} ganhou'
    elif player1.SÍMBOLO == 'Papel':
        if player2.SÍMBOLO == 'Pedra':
            resultado = f'{player1.NOME} ganhou'
        elif player2.SÍMBOLO == 'Tesoura':
            resultado = f'{player2.NOME} ganhou'

    return resultado
















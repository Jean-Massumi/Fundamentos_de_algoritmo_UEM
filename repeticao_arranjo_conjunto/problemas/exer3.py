# Análise:
#   Determinar quantos reais Pedro deverá usar em um certo período.

# Definição:
#   O controle de gastos de Pedro tem tres componentes(Saldo da conta, gastos ,recebimentos) por isso
#   será repesentado por uma estrutura.

from dataclasses import dataclass

@dataclass
class Conta:
    '''
        Indica as entradas e saidas no saldo da conta.
    '''
    SALDO : float
    GASTOS : list[float]
    RECEBIMENTOS : list[float]

def controle_gasto(c:Conta) -> str:
    '''
        Calcular quanto Pedro deve doar.

        Se a *Saldo* < 0 , deve doar +10 reias
    
    Exemplos:
    >>> controle_gasto(Conta(200, [143.7, 61.9, 9.5, 56.8], [12, 6.5, 22.3]))
    'Pedro deverá doar 10 reais'
    >>> controle_gasto(Conta(300, [143.7, 61.9, 9.5, 56.8], [12, 6.5, 22.3]))
    'Pedro deverá doar 0 reais'
    '''
    doacao = 0

    for saida in c.GASTOS:
        c.SALDO -= saida
    for entrada in c.RECEBIMENTOS:
        c.SALDO += entrada

    if c.SALDO < 0:
        doacao += 10

    return f'Pedro deverá doar {doacao} reais'

























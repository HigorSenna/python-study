"""
PEP8 - Python Enhancement Proposal
Propostas de melhorias para a linguagem python

[1] - Utilize Camel Case para nomes de classes;
==================================================================================================
[2] - Utilize nomes em minusculos separados por underline para funções ou variáveis
==================================================================================================
[3] - [3] - UTILIZE 4 ESPAÇOS PARA INDENTAÇÃO (NÃO É RECOMENDADO UTILIZAR O TAB,
pois tem configurações diferentes em computadores diferentes)
==================================================================================================
[4] - Linhas em branco
    . Separar funções e definições de classe com duas linhas em branco;
    . Métodos dentro de uma classe devem ser separados com uma unica linha em branco
==================================================================================================
[5] - Imports devem sempre ser feitos em linhas separadas

Import errado:

 import sys,os

Import CORRETO

import sys
import os

Não há problemas em utilizar:

from types import StringType, ListType pois nesse caso estamos importanto tipos especificos

Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:

from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)

Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentarios ou
docstrings e antes de constantes ou variáveis globais

==================================================================================================

[6] - Espaços em expressoes e intruções

Nao faça:

funcao( algo[ 1 ], { outro: 2 } )
funcao (1)

Faça:

funcao(algo[1], {outro: 2})
funcao(1)



The Zen of python - import this
"""

""" [1] - Utilize Camel Case para nomes de classes """


class Calculator:
    pass


class ScientificCalculator:
    pass


""" [2] - Utilize nomes em minusculos separados por underline para funções ou variáveis """


def sum_one():
    pass


def soma_two():
    pass


number = 4

odd_number = 5


"""" [3] - UTILIZE 4 ESPAÇOS PARA INDENTAÇÃO (NÃO É RECOMENDADO UTILIZAR O TAB, 
pois tem configurações diferentes em computadores diferentes) """

if 'a' in 'banana':
    print('tem')
    print('la')

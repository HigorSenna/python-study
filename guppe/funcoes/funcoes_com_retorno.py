"""
Funcoes com retorno

OBS: Quando uma função não retorna nenhum valor, o retorno é none
"""


def hello():
    print('Hello')


var = hello()
print(f'Retorno: {var}')


def hello_world():
    return "Hello World"


print(f'Retorno do hello_world: {hello_world()}')


# Podemos ter em uma funcao com diferentes tipos de retorno

def nova_funcao():
    variavel = False
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'


print(nova_funcao())


from random import random

# Funcao random é PSEUDO-RANDÔMICO(pode haver repetição) entre 0 e 1


def jogar_moeda():
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'


print(jogar_moeda())

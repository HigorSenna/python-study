"""
Funções de maior grandeza- Higher Order Functions - HOF

- Quando uma linguagem de programação suporte HOF, indica que podemos ter funções
que rtornam outras funções como resultado e podemos passar funções como argumentos para outras funções.
Podemos tambem criar variaveis do tipo de funções
"""


def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def calcular(num1, num2, funcao):
    return funcao(num1, num2)


print(calcular(2, 2, subtrair))
print(calcular(2, 2, somar))


# Podemos ter funcoes dentro de funcoes (Nested Functions)


from random import choice


def cumprimentar(pessoa):
    def humor():
        return choice(('E ai ', 'Suma daqui', 'Gosto muito de voce '))
    return humor() + pessoa


print(cumprimentar('Higor'))

cump = cumprimentar
print(cump('aaa'))


# Funcoes Internar - Inner Funcions (Podem acessar o escopo de funçoes externas)

def rir(pessoa):
    def dar_risada():
        risada = choice(('hahaha', 'ehehehe', 'kkkkkk'))
        return f'{risada} {pessoa}'
    return dar_risada()


print(rir('Higor'))
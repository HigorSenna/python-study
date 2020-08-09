"""
Documentação com Docstrings

Para verificar documentações de funçoes proprias, devo utilizar o TERMINAL(CONSOLE) PYTHON e executar

nome_funcao__doc__

ou

help(nome_funcao)

"""


def hello_world():
    """ Função simples que retorna a string 'Hello World' """
    return 'Hello World'


def exponencial(numero, potencia=2):
    """
    :param numero: valor para ser elevado
    :param potencia: valor dafault = 2
    :return: retorna a potencia do numero
    """
    return numero ** potencia

"""
Lançando os proprios erros com raise

raise -> Lança exceções

OBS: O raise não é uma função, é uma PALAVRA RESERVADA

Forma geral de ulitização:

raise TipoDeErro('Mensagem de erro')
"""


def colorir(texto, cor):
    cores = 'verde', 'amarelo', 'azul', 'branco'
    if type(texto) is not str:
        raise TypeError('Texto precisa ser string')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser string')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre: {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')


colorir('Teste', 'amarelo')

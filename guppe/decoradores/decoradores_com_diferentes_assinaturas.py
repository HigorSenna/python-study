"""
Decorators com difertentes assinaturas

"""


def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar


@gritar
def saudar(nome):
    return f'Olá, eu sou o/a {nome}'


print(saudar('Higor'))


@gritar  # Retorna erro pois a Decorator Function espera apenas um parâmetro
def pedir(principal, acompanhamento):
    return f'Olá, gostaria de {principal}, acompanhado de {acompanhamento}'


# print(pedir('Arroz', 'Picanha'))


# Refatorando para aceitar multiplos parâmetros (Decorator Pattern)

def gritar_certo(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar


@gritar_certo  # Funciona sem problemas pois a Decorator Function recebe infinitos parâmetros
def pedir_certo(principal, acompanhamento):
    return f'Olá, gostaria de {principal}, acompanhado de {acompanhamento}'


print(pedir_certo('Arroz', 'Picanha'))


# Decorators com argumentos

def verifica_primeiro_arumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto, primeiro arumento precisa ser {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna


@verifica_primeiro_arumento('pizza')
def exibir_comida(*args):
    print(args)


print(exibir_comida('Teste', 'pizza'))
print(exibir_comida('pizza', 'churras'))

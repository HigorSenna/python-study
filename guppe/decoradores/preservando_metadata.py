"""
Preservando metadatas com Wraps

Metadados -> são dados intrísecos em arquivos
    - Informacoes contidas nos bytes dos arquivos

wraps -> funcoes que envolvem elementos com diversas funcionalidaes
"""


# Problema

def ver_log(funcao):
    def logar(*args, **kwargs):
        """Eu sou uma função(logar) dentro de outra"""
        print(f'Você está chamando {funcao.__name__}')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def somar(a, b):
    """Soma dois números."""
    return a + b


print(somar(10, 30))

print(somar.__name__)  # Metadados estão sendo alterados por causa do decorator
print(somar.__doc__)   # Metadados estão sendo alterados por causa do decorator


# Resolução do problema


from functools import wraps


def ver_log_certo(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        """Eu sou uma função(logar) dentro de outra"""
        print(f'Você está chamando {funcao.__name__}')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log_certo
def somar_certo(a, b):
    """Soma dois números."""
    return a + b


print('===================================')
print(somar_certo(10, 30))

print(somar_certo.__name__)  # Metadados estão CORRETOS por causa do @wraps
print(somar_certo.__doc__)   # Metadados estão CORRETOS por causa do @wraps

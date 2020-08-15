"""
Decorators

- São funções
- Evoluem outras funções e aprimotam seus comportamentos
- São exemplos de HOF
- Tem uma sintaxe propria, usando @(Syntact Sugar)
"""

# Decorator (Forma nao recomendada)


def ser_educado(funcao):  # Decorando a 'funcao' com a ser_educado
    def ser():
        print('Foi um prazer te conhecer')
        funcao()
        print('Até mais')
    return ser  # Retorna a funcao e nao a EXECUÇÃO da função


def saudar():
    print('Seja bem vindo')


teste = ser_educado(saudar)
teste()


# Forma recomendada

def ser_educado(funcao):  # Decorator Function
    def ser():
        print('Foi um prazer te conhecer')
        funcao()
        print('Até mais')
    return ser  # Retorna a funcao e nao a EXECUÇÃO da função


@ser_educado # Decorator
def saudar():
    print('Seja bem vindo')


saudar()



"""
Definindo Funcoes

def nome_da_funcao(parametros_da_funcao):
    implementacao_da_funcao

nome_da_funcao -> SEMPRE com letras minusculas, separados por underline(Snake Case)

"""

# Exemplo de utilização

cores = ['verde', 'amarelo', 'azul']

# Utilizando função integrada (Built-in) do python, print()
print(cores)


def hello_world():
    print('Hello World')


hello_world()

# Podemos criar variáveis do tipo de uma função e executar esta função através da variável
# OBS: Nao é uma boa prática
hello = hello_world
hello()

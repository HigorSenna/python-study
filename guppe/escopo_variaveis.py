"""
Escopo de variáveis

Dois casos de escopo:

1 - Variáveis globais
2 - Variaveis locais

Para declarar variavel em python, fazemos:

nome_da_variavel = valor

Python é uma linguagem de tipagem dinâmica, isso significa que nao colocamos tipo de dados
na variavel. Este tipo é inferido ao atribuirmos valor a mesma.

"""
numero = 42  # Exemplo de variavel global

if numero > 10:
    novo = numero + 10  # Variavel 'novo' é local
    print(novo)



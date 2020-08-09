"""
Funcoes com parâmetro

Ordem de declarção de parâmetros:

 1 - Parâmetros obrigatorios

"""

def obter_nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'


print(obter_nome_completo('Angelina', 'Jolie'))


# Argumentos nomeados

print(obter_nome_completo(sobrenome='Jolie', nome='Angelia'))
print(obter_nome_completo(nome='Angelia', sobrenome='Jolie'))


def quadrado(numero):
    return numero ** 2


print(quadrado(7))
print(quadrado(8))
print(quadrado(2))


def soma(a, b):
    return a + b


print(soma(1, 3))




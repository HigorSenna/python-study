"""
Entendendo o *args

 - O *args é um parametro de entrada. Isso significa que voce podera chama-lo de qualquer coisa
 desde que começe com o asterisco

 Exemplo:

 *xis
 *qualquer_coisa
 *any

 Por convenção, adotamos sempre *args para defini-lo

 - O parametro *args coloca os valores extras informados como entrada em uma TUPLA
"""


# Exemplos


def soma(num1, num2, num3, num4):
    return num1 + num2 + num3 + num4


print(soma(2, 2, 2, 2))


def somar_tudo(*args):
    total = 0
    for valor in args:
        total += valor
    return total


def somar_tudo_clean(*args):
    return sum(args)


print(somar_tudo(1, 2, 3, 4, 5, 6, 7, 8))
print(somar_tudo())
print(somar_tudo_clean(1, 2, 3, 4, 5, 6, 7, 8))
print(somar_tudo_clean())

# Desempacotar

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(somar_tudo(*lista))
print(somar_tudo_clean(*lista))

tupla = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

print(somar_tudo(*tupla))
print(somar_tudo_clean(*tupla))

set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

print(somar_tudo(*set1))
print(somar_tudo_clean(*set1))


def verificar_info(*args):
    if 'Teste' in args and 'Testando' in args:
        return 'Bem vindo Teste Testando'
    return 'Não sei quem você é...'


print(verificar_info())
print(verificar_info('Teste', 'Testando'))
print(verificar_info(True, 1.45, 1))

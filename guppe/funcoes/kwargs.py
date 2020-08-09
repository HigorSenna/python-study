"""
Entendendo o **kwargs

 - O kwargs é um parametro de entrada. Isso significa que voce podera chama-lo de qualquer coisa
 desde que começe com o asterisco

 Exemplo:

 **xis
 **qualquer_coisa
 **any

Por convenção, adotamos sempre **kwargs para defini-lo

O **kwargs exige que utilizemos PARAMETROS NOMEADOS e transforma esses parâmetros em um DICIONÁRIO

Ordem de declarção de parâmetros:

 1 - Parâmetros obrigatorios
 2 - *args
 3 - Parâmetros default
 4 - **kwargs

"""


def exibir_cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorite de {pessoa.title()} é {cor}')


exibir_cores_favoritas(marcos='verde', julia='azul', fernanda='azul')
exibir_cores_favoritas()


def cumprimento_especial(**kwargs):
    if 'teste' in kwargs and kwargs.get('teste') == 'Python':
        return 'Você recebeu um cumprimento Pythônico!'

    elif 'teste' in kwargs:
        return f"{kwargs.get('teste')}"

    return 'Não sei quem você é ...'


print(cumprimento_especial())
print(cumprimento_especial(teste='Python'))
print(cumprimento_especial(teste='Python2'))


def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)

    if solteiro:
        print('Solteiro')
    else:
        print('Casado')

    print(kwargs)
    print('==========================')


minha_funcao(8, 'Julia')
minha_funcao(18, 'Felicity', 4, 5, 3, solteiro=True)
minha_funcao(34, 'Felipe', eu='Não', voce='Vai')
minha_funcao(19, 'Carla', 9, 4, 3, java=False, python=True)


# Entenda o por que é importante manter a ordem dos parametros na declaração

def mostra_info_correto(a, b, *args, instrutor='Geek', **kwargs):
    return [a, b, args, instrutor, kwargs]


print(mostra_info_correto(1, 2, 3, sobrenome='Teste', cargo='Analista de sistemas'))


def mostra_info_forma_errada(a, b, instrutor='Geek', *args, **kwargs):
    return [a, b, args, instrutor, kwargs]


print('Desse forma abaixo, o parâmetro instrutor está com o valor 3')
print(mostra_info_forma_errada(1, 2, 3, sobrenome='Teste', cargo='Analista de sistemas'))


# Desempacotar com **kwargs
print('==========================')


def mostrar_nomes(**kwargs):
    return f"{kwargs.get('nome')} {kwargs.get('sobrenome')}"


print(mostrar_nomes(nome='QualquerNome', sobrenome='QualquerSobrenome'))
nomes = {'nome': 'TesteNome', 'sobrenome': 'TesteSobrenome'}

print(mostrar_nomes(**nomes))


def somar_multiplos_numeros(a, b, c):
    print(a + b + c)


lista2 = [1, 2, 3]
tupla2 = (1, 2, 3)
set2 = {1, 2, 3}

somar_multiplos_numeros(*lista2)
somar_multiplos_numeros(*tupla2)
somar_multiplos_numeros(*set2)


dicionario = dict(a=1, b=2, c=3)  # Os nomes da chave em um dicionario devem ser os mesmos nomes dos da funcao

somar_multiplos_numeros(**dicionario)

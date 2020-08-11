"""
Debugando com PDB

PDB -> Python Debugger

"""


# Debug

# Com Pycharm podemos debugar normalmente, apenas colocando o breakpoint na ide


def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor incorreto'
    except ZeroDivisionError:
        return 'Não é possivel fazer divisão por 0'


print(dividir(1, 2))

# Exemplo com PDB (executo com o RUN normal)


import pdb

# Exemplo 1

# Comandos
# l -> para listar onde estamos no codigo
# p -> imprime variavel
# c -> finaliza o debug
# Para ver o valor da variavel é so digitar o nome dela (após ja ter executado)

nome = 'Teste'
sobrenome = 'Testando'
pdb.set_trace()
nome_completo = nome.join(' ').join(sobrenome)
print(nome_completo)

# Exemplo 2

# Comandos
# l -> para listar onde estamos no codigo
# p -> imprime variavel
# c -> finaliza o debug
# Para ver o valor da variavel é so digitar o nome dela (após ja ter executado)


# Pq usar dessa forma?
# Assim fica mais facil de identificar o codigo de debug para remove-lo antes da versão final do app

nome = 'Teste'
sobrenome = 'Testando'
import pdb;pdb.set_trace()
nome_completo = nome.join(' ').join(sobrenome)
print(nome_completo)

# A partir do Python3.7 não é necessario importar a blibioteca pdb, pois o comando de debug foi incorporado
# como funcao built-in, chamado de breakpoint()

# Exemplo 3

# Comandos
# l -> para listar onde estamos no codigo
# p -> imprime variavel
# c -> finaliza o debug
# Para ver o valor da variavel é so digitar o nome dela (após ja ter executado)


nome = 'Teste'
sobrenome = 'Testando'
breakpoint()
nome_completo = nome.join(' ').join(sobrenome)
print(nome_completo)


# OBS: Cuidado com os conflitos entre nomes de variáveis e os comandos do pdb


def soma(l, n, p, c):
    breakpoint()
    return l + n + p + c


print(soma(1, 2, 3, 4))

# Neste caso, ao tentarmos ver o valor da variavel apenas digitando-a, iremos executar os comandos do pdb ao inves de
# ver o valor da variável, para solucionar, basta digitar p {nome_variavel_conflitante} para ver o valor, ex:
# p l   p n   .. etc

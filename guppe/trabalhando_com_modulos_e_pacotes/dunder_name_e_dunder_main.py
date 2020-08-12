"""
Dunder name e Dunder Main

Dunder -> Double Under(underline)

Dunder Name -> __name__
Dunder Main -> __main__

Em Python, são utilizados dunder para criar funções,atributos etc utilizando Double Under para nao gerar conflito
com os nomes desses elementos na programação

Se executarmos um modulo python diretamente na linha de comando, internamente o python atribuirá
a variavel __name__ o valor __main__ indicando que este é o modulo de execução principal
"""

from guppe.trabalhando_com_modulos_e_pacotes import custom_module

"""
Repare no module custom_module, ao importamos o modulo e executarmos por aqui, o print nao é executado pois
o arquivo principal de execução nao é o custom_module.py e sim o dunder_name_e_dunder_main.py
"""
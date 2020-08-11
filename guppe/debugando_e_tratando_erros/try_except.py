"""
Try/Except - Tratamento de erros

forma geral mais simples:

try:
    Execução problematica
except:
    O que deve ser feito em caso de problema
"""

# Tratando um erro generico


try:
    funcao_invalida()
except:
    print('Deu algum problema')

# Tratando um erro especifico


try:
    funcao_invalida()
except NameError as err:
    print(f'Você está usando uma funcão inexistente, erro gerado: {err}')
except ValueError:
    print('Deu outro problema')
except:
    print('Problema desconhecido')

"""
Default Dict

Modulo Collections - Default Dict
"""

# Utilizando

from collections import defaultdict

dicionario = defaultdict(lambda: 0)
print(dicionario)

#  DefaultDict nao dá KeyError quando acesso uma chave que nao existe
# Ao inves disso ele cria chave e seta o valor default passa do no defaultdict(default_value)
var = dicionario['qualquer_chave']

print(dicionario)

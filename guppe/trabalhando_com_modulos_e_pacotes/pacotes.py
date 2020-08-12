"""
Pacotes
- É um diretorio contendo uma coleção de modulos

OBS: Nas verosões 2.x do Python, deveria conter dentro dele um arquivo __init__.py

Nas versões do Python 3.x não é mais obrigatória a utilização deste arquivo, mas normalmente
ainda é utilizado para manter compatibilidade
"""

from guppe.geek import geek1, geek2
from guppe.geek.university import geek3, geek4

print(geek1.funcao1(1, 2))
print(geek2.funcao2())
print(geek3.funcao3())
print(geek4.funcao4())

from guppe.geek.geek1 import funcao1
from guppe.geek.university.geek3 import funcao3
print(funcao1(2, 4))
print(funcao3)

"""
Modulos Built-in (Modulos que ja vem instalados no python)


"""

# Utilizando alias

import random as rdm

print(rdm.random())

from random import *  # Dessa forma nao preciso do prefixo
print(random())


# Alias para funcao

from random import randint as rdi

print(rdi(5, 89))


# Costumamos utilizar tuple para importar varias funcoes de um mesmo modulo

from random import (
    random,
    randint,
    shuffle,
    choice
)

print(random())
print(randint(5, 2))
shuffle([1, 2, 3])
print(choice('University'))
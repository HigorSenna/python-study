"""
Modulo Collections - Deque

Podemos dizer que o Deque é uma lista de alta performance
"""

# Utilizando

from collections import deque

deq = deque('Teste')
print(deq)

deq.append('s')
print(deq)

deq.appendleft('O')  # Adiciona elemento no começo
print(deq)

print(deq.popleft())  # Remove e retorna o primeiro elemento

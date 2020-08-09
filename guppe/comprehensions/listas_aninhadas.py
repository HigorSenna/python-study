"""
Listas Aninhadas (Matrizes)


"""

# Exemplos

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(listas)

# Iterando
for elemento in listas:
    for num in elemento:
        print(num, end='')

print('\n =======')

# List Comprehensions

[[print(valor) for valor in lista] for lista in listas]

tabuleiro = [[elemento for elemento in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)
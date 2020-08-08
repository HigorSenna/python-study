"""
Dicionarios
"""

receitas = {'jan': 100, 'fev': 250.0, 'mar': 400}

# Iterando em dicionarios(maps)

for chave in receitas:
    print(chave)

for chave in receitas:
    print(receitas[chave])

for chave in receitas:
    print(f'Em {chave}: recebi R$ {receitas[chave]}')

# Melhor forma de fazer
for chave in receitas.keys():
    print(f'Em {chave}: recebi R$ {receitas[chave]}')


# Ver todas as chaves
receitas.keys()

# Ver os valores
receitas.values()

# Desempacotamento de dicionarios

for chave, valor in receitas.items():
    print(f'chave={chave} e valor={valor}')


# Soma, Valor Maximo, Valor Minimo -> Apenas se todos os valores forem numeros inteiros ou reais

print(sum(receitas.values()))
print(min(receitas.values()))
print(max(receitas.values()))
print(len(receitas))

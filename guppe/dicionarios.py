"""
Dicionários

OBS: Em algumas linguagens os dicionarios python são conhecidos como MAP

Dicionários são coleções do tipo chave/valor

Dicionários são representados por {}

- Tanto a chave como o valor podem ser de qualquer tipo
- Podemos misturar tipos de dados
- NAO PODEMOS ter chaves repetidas
"""

print(type({}))

# Forma 1 (Mais comum)
dicionario1 = {'br': 'Brasil', 'eua': 'Estados unidos'}
print(dicionario1)

# Forma dois (Menos comum)

dicionario2 = dict(br='Brasil', eua='Estados Unidos')
print(dicionario2)


# Acessando elementos
print(dicionario1['br'])  # Caso a chave nao exista, teremos KeyError

# Forma recomendada
print(dicionario2.get('br'))  # Caso a chave nao exista, nao dá erro, retorna o tipo None

russia = dicionario2.get('ru')

if russia:
    print('Encontrei a Russia')
else:
    print('Nao encontrei a Russia')

# Valor default no get
dicionario1.get('ru', 'Russia')  # Caso nao encontre, o valor default será Russia


# Verificar se a CHAVE está no dicionario
print('br' in dicionario2)

# Podemos utilizar qualquer tipo de dado:

localidades = {
    (35.481284, 39.489148): 'Escritório em Tókio',
    (40.481284, 50.489148): 'Escritório em Nova York',
    (56.481284, 80.489148): 'Escritório em São Paulo'
}

print(localidades)
print(localidades.get((35.481284, 39.489148)))

# Adicionando elementos

receitas = {'jan': 120.0, 'fev': 185.8}

print(receitas)

receitas['mar'] = 400  # Forma mais comum de adicionar

print(receitas)
# ou
nova_receita = {'abr': 800}
receitas.update(nova_receita)

print(receitas)

# Atualizando dados

receitas['abr'] = 550
# ou
receitas.update({'abr': 500})

# Remover dados

receitas2 = {'jan': 120.0, 'fev': 185.8}
valor_removido = receitas2.pop('jan')  # Caso nao exista a chave, recebemos KeyError
print(valor_removido)

# ou

del receitas2['fev']  # # Caso nao exista a chave, recebemos KeyError

# Exemplo Carrinho de Compras Utilizando Listas
carrinho = []
produto1 = ['Playstation 5', 1, 6000.00]
produto2 = ['God of War 4', 1, 230.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Exemplo Carrinho de Compras Utilizando Dicionario

carrinho2 = []
produto11 = {'nome': 'Playstation 5', 'quantidade': 1, 'preco': 6000.00}
produto22 = {'nome': 'God of War 4', 'quantidade': 1, 'preco': 230.00}

carrinho2.append(produto11)
carrinho2.append(produto22)
print(carrinho2)

# Metodos de dicionarios

dicionario3 = {'a': 1, 'b': 2, 'c': 3}
novo_dicionario = dicionario3  # Shallow copy
novo_dicionario['d'] = 4

# Forma nao usual de criação de dicionarios

dicionario4 = {}.fromkeys('a', 'b')  # chave, valor
print(dicionario4)

dicionario5 = {}.fromkeys(['pontos', 'nome', 'email'], 'desconhecido')
print(dicionario5)

dicionario6 = {}.fromkeys('teste', 'desconhecido') 
print(dicionario6)

# O Metodo fromkeys recebe dois parametros: um iteravel e um valor,
# ele vai gerar para cada valor do iteravel uma chave e ira atribuir a esta chave o valor informado

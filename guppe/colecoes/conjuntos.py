"""
Conjuntos

 - Conjuntos em qualquer linguagem de programacao estamos fazendo
referência a teoria dos conjuntos em matemática

No python, os conjuntos são chamados de Sets.

- Sets nao possuem valores duplicas
- Sets nao possuem valores ordenados
- Elementos nao sao acessados via indice

Sets sao referenciados em pythons com chaves {}

Diferença entre Sets e Dicionários
   - Um dicionário tem chave/valor
   - um Set tem apenas valor
"""

# Definindo um Set:

# Forma 1
s = set({1, 2, 3, 4, 5, 6, 7, 1, 2, 3})

# Ao criar um Set, caso seja adicionao um valor ja existente, o mesmo será ignorado sem gerar erros

# Forma 2 - Mais comum
s2 = {1, 2, 3, 4}

# Removendo itens duplicados da lista

print('# Removendo itens duplicados da lista')
lista1 = [1, 2, 3, 1, 2]
print(lista1)
s3 = set(lista1)
print(s3)
print('======================================')

# Contains
print('# Contains')
if 3 in s2:
    print('Tem o 3')
else:
    print('Nao tem o 3')
print('======================================')

# Importante lembrar que não temos ordenação
# Listas aceitam valores duplicados, entao temos 10 elementos
print('# Importante lembrar que não temos ordenação')
lista2 = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print(f'Lista: {lista2} com {len(lista2)} elementos')

# Tuplas aceitam valores duplicados, entao temos 10 elementos
tupla = 99, 2, 34, 23, 2, 12, 1, 44, 5, 34
print(f'Tupla: {tupla} com {len(tupla)} elementos')

# Dicionarios nao aceitam chaves duplicadas, entao temos 8 elementos
dicionario = {}.fromkeys([99, 2, 34, 23, 2, 12, 1, 44, 5, 34], 'dicio')
print(f'Dicionario: {dicionario} com {len(dicionario)} elementos')

# Sets nao aceitam valores duplicados, entao temos 8 elementos
set1 = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
print(f'Set: {set1} com {len(set1)} elementos')  # Nao é exibido na ordem que foi declarado
print('======================================')

# Sets aceitam qualquer tipo de dado
print('# Sets aceitam qualquer tipo de dado')
set3 = {1, True, 1.48, 'b'}
print(set3)
print('======================================')

# Iterando
print('# Iterando')
for valor in set3:
    print(valor)
print('======================================')

# Adicionar elementos

print('# Adicionar elementos')
set3.add('c')
print(set3)
print('======================================')

# Remover elementos

print('# Remover elementos')
set3.remove('c')  # Se o valor nao existir, retorna KeyError
# ou
set3.discard(True)  # Se o valor nao existir, NAO retorna erro
print(set3)
print('======================================')

# Copiar Sets
# Tem Shallow Copy e Deep Copy.
# meuset = outroset e setnovo = meuset.copy()

# Remover todos os itens
set1.clear()

# Metodos matematicos
print('# Metodos matematicos')
estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', ' Gustavo', 'Julia', 'Ana', 'Patricia'}

# Union
print('# Union')

unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)
# ou

unicos2 = estudantes_python | estudantes_java
print(unicos2)

print('======================================')

# Gerar um set de estudantes que estão em ambos os cursos(interseção)

print('# Gerar um set de estudantes que estão em ambos os cursos(interseção)')
ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

# ou

ambos2 = estudantes_python & estudantes_java
print(ambos2)
print('======================================')

print('# Gerar um set de estudantes de um curso que nao estao no outro (diferenca)')
so_python = estudantes_python.difference(estudantes_java)
print(f'so python: {so_python}')

so_java = estudantes_java.difference(estudantes_python)
print(f'so java: {so_java}')

print('======================================')

# Soma, Valor Maximo, Valor Minimo -> Apenas se todos os valores forem numeros inteiros ou reais
print('# Soma, Valor Maximo, Valor Minimo -> Apenas se todos os valores forem numeros inteiros ou reais')

numeros_set = {1, 2, 3, 4, 5}
print(f'soma: {sum(numeros_set)}')
print(f'max: {max(numeros_set)}')
print(f'min: {min(numeros_set)}')
print(f'len: {len(numeros_set)}')

print('======================================')

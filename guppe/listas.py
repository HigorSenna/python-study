"""
Listas Python

Listas em python funcionam como arrays, com a diferença
de serem dinamicos e tambem de podermos colocar QUALQUER tipo de dado

OBS:
- Dinâmico: Não possuem tamanho fixo; Ou seja podemos criar a lista
e simplesmente ir adicionando elementos; (enquanto estiver memória disponível)

- Qualquer tipo de dado: Nao possuem tipo de dado fixo, ou seja, podemos colocar qualquer tipo de dado
na mesma lista.
"""

type([])

lista1 = [1, 2, 3, 4, 5, 99, 23, 42, 15, 99]
lista2 = ['G', 's', 'L']
lista3 = []
lista4 = list(range(11))
lista5 = list('Teste')

#  Facilmente encontrando se um elemento está na lista
if 8 in lista4:
    print('Encontrei o 8')
else:
    print('Nao encontrei o 8')

#  Ordenar lista

lista1.sort()
print(lista1)

#  Contar numero de ocorrencias de um valor em uma lista
print(lista1.count(99))

#  Adicionar elementos

lista1.append(42)  # append só adiciona um elemento por vez

#  Adicionando uma lista dentro de  outra lista
lista1.append([8, 3, 1])

# Econtrando uma lista dentro de outra lista

if [8, 3, 1] in lista1:
    print('Encontrei a lista')
else:
    print('ao encontrei a lista')

#  Coloca cada elementro passado como valor adicional da lista.. (Nao vira uma lista dentro da lista)
lista1.extend([123, 44, 67])

#  Inserir elemento na lista informando a posicao do indice
#  Nao subistitui o valor anterior que estava na posicao do indice, ele 'ele é deslocado pra a direita da lista'
lista1.insert(2, 'Novo valor')

#  Juntar listas
lista6 = lista1 + lista2
# ou
lista1.extend(lista2)

#  Inverter lista
lista1.reverse()
# ou
nova_lista_invertida = lista1[::-1]

#  Copiar uma lista
lista7 = lista1.copy()

#  Tamando da lista
len(lista1)

#  Remover ultimo elemento da lista
#  OBS: Remove e retorna o ultimo elemento
lista7.pop()

#  Remover elemento pelo indice
lista5.pop(2)

#  Remover todos os elementos da lista(zerar a lista)
lista8 = lista1.copy()
lista8.clear()

#  Repetir elementos em uma lista
lista9 = lista1.copy()
lista9 *= 3

print(lista9)

#  Converter string para lista
curso = 'Programacao em Python'
curso = curso.split()  # Por padrao o split separa os elementos da lista pelo espaço entre elas
curso2 = 'Programacao,em,Python'
curso2 = curso2.split(',')

#  Converter lista em string
lista10 = ['Programcao', 'em', 'Python']
lista10_string = ' '.join(lista10)  # Coloca o espaco entre cada elemento da lista e transforma em string


#  Iterando em listas
#  Exemplo 1
lista11 = ['Teste', True, 4.456, 489, [1, 2, 3]]

for elememento in lista11:
    print(elememento)

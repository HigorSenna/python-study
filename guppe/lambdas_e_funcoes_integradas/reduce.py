"""
Reduce

OBS: A partir do Python3+ a funcao reduce nao é mais uma função integrada(built-in).
Agora temos que importar e utilizar esta função a partir do modulo 'functools'

Guido van Rossum(Criador do python): "Utilize a função reduce() se você realmente precisar dela.
99% das vezes um loop for é mais legível"

Ao contrario dos metodos map() e filter(), o reduce() recebe no primeiro parâmetro, uma funcao
que espera dois parametros ao invés de um

reduce():
   Passo 1: res1 = f(a1, a2)  Aplica a funcao nos dois primeiros elementos da coleção e guarda o resultado
   Passo 2: res2 = f(res1, a3) Aplica a funcao passando o resultado do passo1 mais o terceiro elemento e guarda
   o resultado e isso é repetido ate o final

"""

# Multiplicar todos os numeros de uma lista

from functools import reduce

dados = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29]

# Para utilizar reduce() precisamos de uma funcao que receba dois parâmetros

multi = lambda x, y: x * y

res = reduce(multi, dados)
print(res)


# Utilizando loop normal

res1 = 1
for n in dados:
    res1 *= n

print(res1)

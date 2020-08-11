"""
Len. Abs, Sum, Round

len() -> retona o tamanho de um iteravel

abs() -> Retorna o valor absoluta de um número inteiro ou real

sum() -> Recebe como parâmetro um iteravel, podendo receber um iteravel, retorna a soma total dos elementos,
 incluindo o valor inicial
 OBS: O valor inicial default é 0

round() -> retorna um numero arredondado para n digito de precisao após a casa decimal. Se a precisao nao for informada
retorna o inteiro mais próximo da entrada.

"""

print(len('Teste'))

# Ao utilizar a funcao len(), por baixo dos panos, o python faz:
# Dunder __len()__
'Teste'.__len__()


print(abs(-5))
print(abs(3.14))
print(abs(-3.14))


print(sum([1, 2, 3, 4, 5]))
print(sum([1, 2, 3, 4, 5], 10))
print(sum({'a': 1, 'b': 2, 'c': 3}.values()))


print(round(10.2))
print(round(10.5))
print(round(10.6))
print(round(1.2121212121, 2))
print(round(1.219999999, 2))


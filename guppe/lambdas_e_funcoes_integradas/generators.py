"""
Generators

Não vimos Tuple Comprehensions porque elas se chama Generators
"""

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano']

# List Comprehension
resultado_list = [nome[0] == 'C' for nome in nomes]
print(type(resultado_list))
print(list(resultado_list))

# Generator
# Ocupa menos recurso em memória
resultado_generator = (nome[0] == 'C' for nome in nomes)
print(type(resultado_generator))
print(list(resultado_generator))  # OBS: Após utilizar a função map, depois da primeira utilização do resultado,ele zera
print(list(resultado_generator))


from sys import getsizeof

list_comp = getsizeof([x * 10 for x in range(1000)])
set_comp = getsizeof({x * 10 for x in range(1000)})
dic_comp = getsizeof({x: x * 10 for x in range(1000)})
gen = getsizeof(x * 10 for x in range(1000))

print('Para fazer a mesma tarefa gastamos em memória: ')
print(f'List Comprehension: {list_comp} bytes')
print(f'Set Comprehension: {set_comp} bytes')
print(f'Dictionary Comprehension: {dic_comp} bytes')
print(f'Generator Expression: {gen} bytes')


# Iterando no Generator

gen = (x * 10 for x in range(1000))
for num in gen:
    print(num)


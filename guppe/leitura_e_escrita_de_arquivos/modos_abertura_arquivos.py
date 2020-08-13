"""
Modos de abertura de arquivos

r -> leitura
w -> escrita -> sobrescreve caso o arquivo ja exista
x -> abre para escrita somente se o arquivo nao existir, caso exista gera FileExistsError
a -> abre para escrita, adicionando o conteudo no final do arquivo caso exista. Caso o arquivo não exista, será criado.
Caso já exista, o conteúdo é adicionado no final.

+ -> abre para o modo de atualização leitura e escrita, para utilizar devemos usar precedido de alguma dos tipos
anteriores: ex:
r+ (r > leitura,  + -> escrita)
w+ (w -> escrita, + -> leitura), etc

https://docs.python.org/3/library/functions.html#open
"""
try:
    with open('teste1.txt', 'x') as arquivo1:
        arquivo1.write('Teste de conteudo')
except FileExistsError:
    print('Arquivo ja existe')

with open('teste2.txt', 'a') as arquivo1:
    arquivo1.write('Teste de conteudo\n')

# Escrevendo no inicio do arquivo -> NÃO FUNCIONA, Abrindo como 'a' é SEMPRE no final
with open('teste2.txt', 'a') as arquivo1:
    arquivo1.seek(0)  # como está no modo 'a' nao conseguimos controlar o cursor
    arquivo1.write('Teste de conteudo INICIO\n')

# OBS com as aberturas default, nao conseguimos escrever no topo do arquivo, sempre no final


# ESCRITA E LEITURA
with open('teste2.txt', 'a+') as arquivo1:
    arquivo1.write('Teste de conteudo INICIO\n')
    arquivo1.seek(0)
    print(arquivo1.read())


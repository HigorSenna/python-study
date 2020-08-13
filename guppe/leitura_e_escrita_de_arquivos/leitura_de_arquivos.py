"""
Leitura de arquivos

Para ler um aruivo em Python, utilizamos a função integrada open().

open() -> Na forma mais simples de utilização passamos apenas o caminho/nome do arquivo como parâmetro de entrada.
Essa função retorna um _io.TextIOWrapper.

# OBS: por padrão a função open() abre o arquivo para LEITURA. Caso arquivo nao exista, teremos o erro
FileNotFoundError

mode r -> modo de leitura
mode w -> modo de escrita

https://docs.python.org/3/library/functions.html#open
"""

arquivo = open('texto.txt')
print(arquivo)
#  <_io.TextIOWrapper name='texto.txt' mode='r' encoding='UTF-8'>
# mode r -> modo de leitura
# encoding='UTF-8' -> reconhece os caracteres especiais
print(type(arquivo))

# Lendo o arquivo
print(arquivo.read())

# OBS: O Python utiliza um recurso para trabalhar com arquivos chamado cursor, Esse cursos funciona
# como o cursos quando estamos escrevendo um texto comum, quando eu leio um arquivo, o cursos vai pro final, sendo assim
# ao ler o arquivo, nao consigo ler novamente logo em seguida
print(arquivo.read())
arquivo.close()

print("===============================")

arquivo = open('texto.txt')
all_text = arquivo.read()
print(all_text)
print(all_text)
arquivo.close()

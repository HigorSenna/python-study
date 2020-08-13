"""
Seek e Cursors

seek() -> é utilizada para movimentar o cursor pelo arquivo

"""

arquivo = open('texto.txt')

print(arquivo.read())  # Le todo o arquivo de uma vez
print("=============================")
arquivo.seek(0)
print(arquivo.read(50))  # Le os PRIMEIROS 50 caracteres do arquivo
print("=============================")
# Movimentando o cursor

arquivo.seek(0)

print(arquivo.read())
print("=============================")

arquivo.seek(12)

print(arquivo.read())
print("=============================")
# Ler o arquivo linha a linha

arquivo.seek(0)
print(arquivo.readline())
print("=============================")
print(arquivo.readline())
print("=============================")
print(arquivo.readline())
print("=============================")

# Ler linhaS
arquivo.seek(0)
linhas = arquivo.readlines()  # coloca cada linha como um elemento da lista
print(linhas)
print("=============================")
print(arquivo.closed)  # Verifica se o arquivo está fechado
print("=============================")
arquivo.close()

print(arquivo.closed)
print("=============================")
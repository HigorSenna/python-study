"""
Sistema de Arquivos e Navegação

Para fazer uso de manipulação de arquivos do sistema operacional, precisamos usar o modulo "os"
"""

import os

# Pega o diretorio atual (current work directory) -> caminho absoluto
print(os.getcwd())

# Mudar o diretório
os.chdir("../")
print(os.getcwd())

# Podemos checar se um diretorio é absoluto ou relativo

print(os.path.isabs('/home/geek/'))  # True
print(os.path.isabs('/home/geek/'))  # True
print(os.path.isabs('home/geek/'))   # False

# OBS PARA WINDOWS:

print(os.path.isabs('C:\\Users'))

# Identificando o sistema operacional
print(os.name)  # posix(Linux e Mac), nt (Windows)

# Identificando mais detalhes do sistema operacional

print(os.uname())  # No windows nao temos essa funcao

# Join para diretorios

print(os.getcwd())
res = os.path.join(os.getcwd(), 'OutroDir', 'OutroOutroDir')
print(res)

# Listando arquivos e diretorios

print(os.listdir())
print(os.listdir('/etc'))

# Listando arquivos e diretorios com mais detalhes
scanner = os.scandir('/etc')
arquivos = list(scanner)
print(arquivos[0].name)
print(dir(arquivos[0]))

# OBS: Após utilizar o scandir(), devemos fechar

scanner.close()

import sys
print(sys.platform)
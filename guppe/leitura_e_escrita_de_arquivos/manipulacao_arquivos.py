"""
Manipulação arquivos e Diretórios


"""

# Descrobrindo se um arquivo ou Diretório existe

import os

print(os.path.exists('teste1.txt'))
print(os.path.exists('leitura_e_escrita_de_arquivos/teste1.txt'))
print(os.path.exists('../leitura_e_escrita_de_arquivos/teste1.txt'))

# Criando arquivos

# Forma 1
open('arq1.txt', 'w').close()

# Forma 2

open('arq2.txt', 'a').close()

# Forma 3

with open('arq3.txt', 'w') as arq3:
    pass

# Só funciona no LINUX
# os.mknod('../leitura_e_escrita_de_arquivos/arq4.txt') # Se o arquivo já existir, da erro



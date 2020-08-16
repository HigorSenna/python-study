"""
Escrevendo arquivos CSV

writer()
writerow() -> escreve uma linha
"""

from csv import writer
from typing import TextIO

"""
with open('filmes.csv', 'a', encoding='utf-8', newline='') as arquivo:    
    escritor_csv = writer(arquivo)
    filme = None
    escritor_csv.writerow(['Título', 'Gênero', 'Duração'])
    while filme != 'sair':
        filme = input('Informe o nome do filme:')
        if filme != 'sair':
            duracao = input('Informe a duracao do filme (em minutos): ')
            genero = input('Informe o gênero do filme: ')
            escritor_csv.writerow([filme, genero, duracao])
"""


# DictWriter

from csv import DictWriter

with open('filmes3.csv', 'a+', encoding='utf-8', newline='') as arquivo:

    cabecalho = ['Título', 'Gênero', 'Duração']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)

    arquivo.seek(0)
    if len(arquivo.read()) == 0:
        escritor_csv.writeheader()

    filme = None
    while filme != 'sair':
        filme = input('Informe o nome do filme:')
        if filme != 'sair':
            genero = input('Informe o gênero do filme: ')
            duracao = input('Informe a duracao do filme (em minutos): ')

            # As chaves precisam ser as mesmas do cabecalho
            # escritor_csv.writerow({"Título": filme, "Gênero": genero, "Duração": duracao})
            escritor_csv.writerow({cabecalho[0]: filme, cabecalho[1]: genero, cabecalho[2]: duracao})

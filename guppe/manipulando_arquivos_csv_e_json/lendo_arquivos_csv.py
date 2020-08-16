"""
Lendo arquivos CSV

CSV - Comma Separeted Values
    - Podemos ter outro tipos de separadores de CSV além da virgula

https://dados.gov/dataset -> dados fornecidos pelo governo federal

A linguagem Python possui duas formas diferentes para ler dados em arquivos CSV:
    - reader -> Permite que iteremos sobre as linhas do arquivo CSV como listas;
    - DictReader -> Permite que iteremos sobre as linhas do arquivo CSV como OrderedDicts;
"""

# Possivel de se trabalhar, mas nao é o ideial (trabalhoso)
with open('lutadores.csv', encoding='utf-8') as arquivo:
    dados = arquivo.read()
    dados = dados.split(',')[2:]
    print(dados)


# Reader
print('============================================')
from csv import reader

with open('lutadores.csv', encoding='utf-8') as arquivo:
    leitor_csv = reader(arquivo, delimiter=',')  # retorna um Iterator
    next(leitor_csv)  # Pulando o cabeçalho
    for linha in leitor_csv:
        # Cada linha é uma lista
        print(f'{linha[0]} nasceu no(a) {linha[1]} e mede {linha[2]} centimetros')


print('============================================')

# DictReader
# Monta cada item como chave e valor a partir do cabeçalho
from csv import DictReader

with open('lutadores.csv', encoding='utf-8') as arquivo:
    leitor_csv = DictReader(arquivo, delimiter=',')
    for linha in leitor_csv:
        # Cada linha é um OrderedDict
        print(f"{linha.get('Nome')} nasceu no(a) {linha.get('País')} e mede {linha.get('Altura (em cm)')}")

"""
Escrevendo em arquivos

# OBS: Ao abrir um arquivo para leitura, não podemos escrever nele, apenas ler e vice-versa
"""

# Na escrita, caso o arquivo nao exista, ele é criado, caso ele já exista, o anterior será apagado e um novo
# será criado. Dessa forma, todo o conteudo anteior do arquivo é perdido.

with open('texto.txt', 'w') as arquivo:
    arquivo.write('Escrevendo linha 1\n')
    arquivo.write('Escrevendo linha 2\n')


quantidade_linhas = 1000

with open('texto.txt', 'w') as arquivo:
    arquivo.write('Escrevendo linha\n' * quantidade_linhas)

continuar = True

with open('texto.txt', 'w') as arquivo:
    while True:
        texto = input('Informe o dado ou digite sair')
        if texto == 'sair':
            break
        else:
            arquivo.write(texto + '\n')

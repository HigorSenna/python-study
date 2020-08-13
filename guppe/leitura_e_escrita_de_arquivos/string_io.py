"""
StringIO

ATENÇÃO: Para ler ou escrever dados em arquivos do sistema operacional o software precisa ter permissão:
    - Permissao de leitura -> para ler
    - Permissao de escrita-> para escrever

StringIO -> utilizado para ler e criar arquivos em memória
"""

from io import StringIO

mensagem = 'Mensagem normal'

# Podemos criar um arquivo em memória:

arquivo = StringIO(mensagem)

# Agora, tendo o arquivo, podemos utilizar tudo que já sabemos.
print(arquivo.read())
arquivo.write('\nOutro texto')
arquivo.seek(0)
print(arquivo.read())

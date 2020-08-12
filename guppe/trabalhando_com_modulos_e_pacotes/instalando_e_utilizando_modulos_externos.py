"""

Modulos Externos

Utilizamos o gerencidor de pacotes Python chamados Pip - Python Installer Package

Você pode conhecer todos os pacotes externos oficiais em: https://pypi.org

pacote colorama: É utilizado para imprmir textos coloridos no terminal

instalando um module:

pip install nome_do_module
"""

from colorama import init, Fore, Back
init()
print(Fore.GREEN + 'Teste')
print(Back.MAGENTA + 'Teste')


# OBS: Alguns modulos nao funcionam nativamente no windows:

"""
If you’re not on Linux amd64: pydf comes bundled
with a wkhtmltopdf binary which will only work on Linux amd64 architectures. If you’re on another OS or architecture 
your milage may vary, it is likely that you’ll need to supply your own wkhtmltopdf binary and point pydf towards it by
setting the WKHTMLTOPDF_PATH variable.
"""

import pydf

pdf = pydf.generate_pdf('<h1>Teste</h1>')

with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)

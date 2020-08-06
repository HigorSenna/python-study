"""
Estruturas logicas and, or, not, is
"""

ativo = True
logado = False

if ativo and logado:
    print('Bem vindo')
else:
    print('Você precisa ativar sua conta')


if ativo or logado:
    print('Bem vindo')
else:
    print('Você precisa ativar sua conta')


if not ativo:
    print('Voce precisa ativar sua conta')
else:
    print('Sua conta ja esta ativa')

if ativo is True:  # Nao é muito usado, ao inves disso, apenas usar if ativo:
    print('OK')
else:
    print('Voce precisa ativar sua conta')
# Estrutura de Decisão
''' Na estrutura de decisão o código só executa se a condição estipulada for satisfeita'''

if True:
    print('Verdadeiro')

if False:
    print('Falso') # Não será executado porque a condição é falsa.

# Outra condição_ sendo a condição False, os prints do escopo não serão executados, só o de fora.
if 5 < 3:
    print('Olá')
    print('Tudo bem')

print('Até logo!')

# Outra condição_sendo a condição verdadeira, todos os prints serão executados.
if 5 > 3:
    print('Olá')
    print('Tudo bem')

print('Até logo!')

# Concatenando com and
if 5 > 4 and 6 > 7: # as duas condições não foram atendidas. Não imprimiu!
    print('Olá')
    print('Tudo bem')

print('Até logo!')

if 5 > 4 and 6 == 6: # as duas condições foram atendidas. imprimiu!
    print('Olá')
    print('Tudo bem')

print('Até logo!')
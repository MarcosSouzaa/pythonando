# if, else, elif
# elif - Para ele ser executado, precisa que a condição acima dele seja falsa, mas a dele, verdadeira.

media = 1

if media >= 7:
    print('APROVADO')
elif media >= 6:
    print('RECUPERAÇÃO')
elif media >= 2:
    print('REPROVADO') 
else:
    print('EXPULSO')
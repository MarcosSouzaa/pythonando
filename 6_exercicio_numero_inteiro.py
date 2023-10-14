# Receba três números inteiros e exiba o maior deles

n1 = int(input('Digite o primeiro número inteiro: '))
n2 = int(input('Digite o segundo número inteiro: '))
n3 = int(input('Digite o terceiro número inteiro: '))

if n1 > n2 and n1 > n3:
    print(f'O número digitado {n1} é maior!')
elif n2 > n1 and n2 > n3:
    print(f'O número digitado {n2} é maior!')
elif n3 > n1 or n3 > n2:
    print(f'O número digitado {n3} é maior!')

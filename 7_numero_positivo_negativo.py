# Receba um número e exiba se ele é positivo ou negativo

num = float(input('Digite um número: '))

if num > 0:
    print(f'O número digitado {num} é positivo!')
elif num < 0:
    print(f'O número digitado {num} é negativo!')
else:
    print('O número é zero!')

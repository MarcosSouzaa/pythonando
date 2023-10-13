'''
Receba 4 notas de um aluno e exiba se ele foi APROVADO (nota >= 6)
Se ele ficou de recuperação (nota >= 4)
se ele foi reprovado(nota < 4)
'''
nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))
nota3 = float(input('Digite a nota 3: '))
nota4 = float(input('Digite a nota 4: '))
print('')
media = (nota1 + nota2 + nota3 + nota4)/4

print("Nota >= 6 = Aprovado")
print("Nota > 4 e < 6 = em Recuperação")
print("Nota < 4 = Reprovado \n")

print('A média do aluno foi:', media)

if media >= 6:
    print(f'Aluno Aprovado com a nota {media}')
elif media >= 4:
    print(f'Aluno em Recuperação com a nota {media}')
else:
    print(f'Aluno Reprovado com a nota {media}')
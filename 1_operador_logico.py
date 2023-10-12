# and, or, not

''' and - Só retorna True se os dois lados forem iguais'''
operador = True and True
print(operador) # True

operador = False and True
print(operador) # False

''' and - Retorna True se um dos dois lados forem verdadeiros'''
operador = False or False
print(operador) # False

operador = False or True
print(operador)  # True

operador = True or False
print(operador)  # True

''' not - inverte as coisas.Ex se algo ´r falso ele transforma em verdadeiro e vice versa'''
operador = not False
print(operador) # True

operador = not True
print(operador) # True

# Operações com and
operador = 5 == 5 and 3 < 2
print(operador) # False

operador = 5 == 5 and 3 > 2
print(operador) # True

# Operações com or
operador = 5 == 7 or 3 > 2
print(operador) # True

operador = 5 == 7 or 3 < 2
print(operador) # False

# Operações com not
operador = not(5 == 7 or 3 < 2) # A operação é falsa, mas o not inverte para True
print(operador) # True

operador = not(5 == 7 or 3 > 2) # A operação é verdadeira, mas o not inverte para False
print(operador) # False
                            
operador = not((5 == 7 or 3 > 2) and (2 == 2 or 5 < 5)) 
print(operador) # False

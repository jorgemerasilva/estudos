"""
Booleanos são um tipo de dado que representa valores de verdade, ou seja, verdadeiro (True) ou falso (False). Eles são amplamente utilizados em programação para controlar o fluxo de execução do código, fazer comparações e tomar decisões com base em condições.

"""

nome = "Jorge Mera da Silva"
idade = 25
é_adulto = idade >= 18

if é_adulto:
    print(f"{nome} é adulto.")
else:
    print(f"{nome} não é adulto.")


#Operadores de comparação retornam valores booleanos. Alguns exemplos de operadores de comparação são:

valor1 = 10
valor2 = 20

# == (igual a)
if valor1 == valor2:
    print(f"{valor1} é igual a {valor2}.")
else:
    print(f"{valor1} não é igual a {valor2}.")

# != (diferente de)
if valor1 != valor2:
    print(f"{valor1} é diferente de {valor2}.")
else:
    print(f"{valor1} não é diferente de {valor2}.")

# > (maior que)
if valor1 > valor2:
    print(f"{valor1} é maior que {valor2}.")
else:
    print(f"{valor1} não é maior que {valor2}.")

# < (menor que)
if valor1 < valor2:
    print(f"{valor1} é menor que {valor2}.")
else:
    print(f"{valor1} não é menor que {valor2}.")

# >= (maior ou igual a)
if valor1 >= valor2:
    print(f"{valor1} é maior ou igual a {valor2}.")
else:
    print(f"{valor1} não é maior ou igual a {valor2}.")

# <= (menor ou igual a)
if valor1 <= valor2:
    print(f"{valor1} é menor ou igual a {valor2}.")
else:
    print(f"{valor1} não é menor ou igual a {valor2}.")



#Operadores lógicos também retornam valores booleanos e são usados para combinar ou inverter condições. Alguns exemplos de operadores lógicos são:

# and (e)
if valor1 == 10 and valor2 == 20:
    print(f"{valor1} é 10 e {valor2} é 20.")
else:
    print(f"{valor1} não é 10 ou {valor2} não é 20.")
    
# or (ou)
if valor1 == 10 or valor2 == 20:
    print(f"{valor1} é 10 ou {valor2} é 20.")
else:
    print(f"{valor1} não é 10 e {valor2} não é 20.")

# not (não)
if not valor1 == 10:
    print(f"{valor1} não é 10.")
else:
    print(f"{valor1} é 10.")
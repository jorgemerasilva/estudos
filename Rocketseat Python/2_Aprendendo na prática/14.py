import math
from math import pow
from modulos.matematica import somar_salarios

raiz_quadrada = math.sqrt(25)
print(f"Raiz quadrada de 25 é {raiz_quadrada}")

potencia = pow(5,2)
print(f"5 elevado  a 2 é {potencia}")

lista = [1200, 1500, 9000]
total = somar_salarios(lista=lista)
print(f"Total: R$ {total:,.2f}")
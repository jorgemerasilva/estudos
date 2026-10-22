numero = 10
try:
    resultado = 10 / numero
except TypeError as e:
    print(e)
except ValueError as e:
    print(e)
    raise ValueError("Tipo de valor incompativel!")
except ZeroDivisionError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f"\nResultado: {resultado}")
finally:
    print("\nPrograma finalizado!")


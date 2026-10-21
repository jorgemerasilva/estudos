lista =[1,2,3,5,8,7,4,56,96,85,75,47]

for num in lista:
    print(num)

tupla = (2,5,8,7,3,69,4)
for num in tupla:
    print(num)

pessoa = {"nome": "jorge", "idade": 31}

for chave, valor in pessoa.items():
    print(f"{chave} - {valor}")

for chave in pessoa.keys():
    print(f"{chave} - {valor}")

for valor in pessoa.values():
    print(f"{valor}")


#For com range()
for numero in range(11):
    print("Número: ", numero)


#For com range e len
salarios = [1500, 6000, 12000, 7000]
for indice in range(0, len(salarios)):
    print(f"Indece: {indice}, Valor: {salarios[indice]}")
    #Indice 0, o valor vai ser 0
    if indice == 0:
        salarios[indice] = 0
        
print(salarios)

#For com enumerate
for indice, valor in enumerate(salarios):
    print(f"{indice}: {valor}")
    #Se o valor for igual a zero mude pra 1000 o valor
    if salarios[indice] == 0:
        salarios[indice] = 1000

print(salarios)
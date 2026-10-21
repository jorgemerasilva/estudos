"""
Listas

"""
minha_lista = ["Jorge", "Lucas", "Kaylanne", "Maria"]

#Exibindo a lista
print("Minha lista de exemplo", minha_lista)

#Exibindo os elemento da lista
print("Primeiro elemento: ", minha_lista[0])
print("Último elemento: ", minha_lista[-1])
print("Segundo elemento: ", minha_lista[2])
print("Fatiar de 0 a 2: ", minha_lista[0:2])


minha_lista.append("joão")            # adiciona no fim
print("Minha lista de exemplo", minha_lista)

minha_lista.extend(["Pedro", "Jesus"])       # adiciona vários
print("Minha lista de exemplo", minha_lista)

minha_lista.insert(0, "Deus")       # insere na posição
print("Minha lista de exemplo", minha_lista)

minha_lista.remove("Kaylanne")            # remove 1ª ocorrência do valor
print("Minha lista de exemplo", minha_lista)

minha_lista.pop()                # remove e retorna o último
print("Minha lista de exemplo", minha_lista)

minha_lista.pop(0)               # remove e retorna pelo índice
print("Minha lista de exemplo", minha_lista)

del minha_lista[0]               # remove pelo índice
print("Minha lista de exemplo", minha_lista)

del minha_lista[1:3]             # remove fatia
print("Minha lista de exemplo", minha_lista)

minha_lista.clear()              # esvazia
print("Minha lista de exemplo", minha_lista)




salarios = [1200, 1500, 2000, 3000, 1200]

salarios.index(1200)             # posição do valor
#Exemplo
indice_do_salario_de_1200 = salarios.index(1200)
print(f"O indice do salário de 1200 é ", indice_do_salario_de_1200)

salarios.count(1)

#Exemplo
ocorrencia_de_1200 = salarios.count(1200)
print(f"Número de ocorrêcias de 1200 é ", ocorrencia_de_1200)

salarios.sort()               # ordena in-place
salarios.sort(reverse=True)
salarios.sort(key=lambda salario: salario)        # ordena por critério
salarios.reverse()
sorted(salarios)              # nova lista ordenada

#Exemplo
ordenados = sorted(salarios, key=lambda salario: salario, reverse=True)
print(f"Lista ordenada: {ordenados}")

reversed(salarios)          # iterador invertido

#Exemplo
invertidos = list(reversed(salarios))

print(invertidos)
# [1200, 3000, 2000, 1500, 1200]

salarios.copy()               # cópia rasa (= lst[:])

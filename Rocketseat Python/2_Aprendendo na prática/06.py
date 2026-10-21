"""
Dicionarios

"""

pessoa = {"nome": "jorge", "idade": 31, "cidade": "Redenção", "estado": "PA"}

#Exibindo dicionario
print("Meu dicionario: ", pessoa)

#Acessando valores por chave
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Cidade:", pessoa["cidade"])
print("Estado:", pessoa["estado"])

#Adicionar chave com valor
pessoa["altura"] = 173.3
print("Meu dicionario: ", pessoa)

#Remover uma par chave-valor
del pessoa["idade"]
print("Meu dicionario: ", pessoa)

#Métodos: keys()
chaves = pessoa.keys()
print("Chaves: ", chaves)

#values()
valores = pessoa.values()
print("Valores: ", valores)

#items()
items = list(pessoa.items())
print("Valores: ", items)
print(f"Primeira chave-valor {items[0][0]} = {items[0][1]}")

#Pra acessar  os valores precisa transformar keys(), values(), items() em list()
#Exemplo:
chaves = list(pessoa.keys())
print(f"Primeira chave: {chaves[0]}")
print(f"Última chave: {chaves[-1]}")

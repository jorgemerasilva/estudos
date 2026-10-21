
def media_notas(lista):
    total = 0
    for num in lista:
        total += float(num)
    return total / len(lista)


lista = [10,9,7,28]
print(f"Lista: {", ".join(str(n) for n in lista[:-1]) + " e " + str(lista[-1])}\nMedia: {media_notas(lista=lista)}")



funcionarios = [
    {"nome": "Jorge", "salario": 15000, "funcao": "Advogado"},
    {"nome": "Kaylanne", "salario": 9000, "funcao": "Biomedica"},
    {"nome": "João Henrique", "salario": 30000, "funcao": "Juiz"}
]

def avaliacao(lista):
    folha_de_pagamento_mensal = 0
    indice_escolhido = 0
    salario_atual = 0
    for indice, funcionario in enumerate(lista):
        folha_de_pagamento_mensal += funcionario["salario"]
        if funcionario["salario"] > salario_atual:
            salario_atual = funcionario["salario"]
            indice_escolhido = indice
    
    return folha_de_pagamento_mensal, indice_escolhido


folha_de_pagamento_mensal, indice_escolhido = avaliacao(funcionarios)
print(f"Funcinario com maior salario: {funcionarios[indice_escolhido]["nome"]} com salário de R$ {funcionarios[indice_escolhido]["salario"]:,.2f}")
print(f"Folha de pagamento mensal: R$ {folha_de_pagamento_mensal:,.2f}")
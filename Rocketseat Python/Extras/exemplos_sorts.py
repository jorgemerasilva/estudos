
funcionarios = [
    {"nome": "Jorge", "salario": 2000, "idade": 30, "avaliacao": 2.5},
    {"nome": "Ana", "salario": 1200, "idade": 21, "avaliacao": 3.5},
    {"nome": "Lucas", "salario": 1500, "idade": 38, "avaliacao": 4.9},
    {"nome": "Pedro", "salario": 3500, "idade": 40, "avaliacao": 5.0},
    {"nome": "Kaylanne", "salario": 7500, "idade": 45, "avaliacao": 4.9}
]

#Melhor salário
funcionarios.sort(
    key=lambda funcionario: funcionario["salario"],
    reverse=True
)
print("\nMaiores salários:")
for funcionario in funcionarios:
    print(f"{funcionario["nome"]} - {funcionario["salario"]} - {funcionario["idade"]} - {funcionario["avaliacao"]}")



#Melhor Avaliação
funcionarios.sort(
    key=lambda funcionario: funcionario["avaliacao"],
    reverse=True
)

print("\nMaiores avaliações:")
for funcionario in funcionarios:
    print(f"{funcionario["nome"]} - {funcionario["salario"]} - {funcionario["idade"]} - {funcionario["avaliacao"]}")
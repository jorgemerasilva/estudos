#F032
def adicionar_tarefa(tarefas, nome_tarefa):
    tarefa = {"tarefa": nome_tarefa, "completada": False}
    tarefas.append(tarefa)
    print(f"\nTarefa {nome_tarefa} foi adicionada com sucesso!")
    return

def ver_tarefas(tarefas):
    print("\nLista de tarefas")
    for indice, tarefa in enumerate(tarefas, start=1):
        status = "X" if tarefa["completada"] else " "
        nome_tarefa = tarefa["tarefa"]
        print(f"\n{indice}.[{status}] {nome_tarefa}")
    return

def atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome_tarefa):
    indice_tarefa_ajustado = int(indice_tarefa) - 1
    if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas):
        tarefas[indice_tarefa_ajustado]["tarefa"] = novo_nome_tarefa
        print(f"Tarefa {indice_tarefa} atualizada para {novo_nome_tarefa}")
    else:
        print("Indice de tarefa inválido!")
    return

tarefas = []

while True:
    print("\nMenur do Gerenciador de lista de tarefas:")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Atualizar tarefa")
    print("4.Completar tarefa")
    print("5. Deletar tarefas completadas")
    print("6. Sair")

    escolha = input("Digite a sua escolha: ")

    if escolha == "1":
        nome_tarefa = input("Digite o nome da tarefa que deseja adicionar: ")
        adicionar_tarefa(tarefas=tarefas, nome_tarefa=nome_tarefa)

    elif escolha == "2":
        ver_tarefas(tarefas=tarefas)

    elif escolha == "3":
        ver_tarefas(tarefas=tarefas)
        indice_tarefa = input("Digite o número da tarefa que deseja atualizar: ")
        novo_nome = input("Digite o novo nome da tarefa: ")
        atualizar_nome_tarefa(tarefas=tarefas, indice_tarefa=indice_tarefa, novo_nome=novo_nome)

    elif escolha == "4":
        pass
    elif escolha == "5":
        pass
    elif escolha == "6":
        print("\nVocê saiu do programa!")
        break
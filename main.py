tarefas = []

def adicionar_tarefa():
    tarefa = input("Digite a nova tarefa: ")
    tarefas.append(tarefa)
    print("Tarefa adicionada!")

def listar_tarefas():
    if len(tarefas) == 0:
        print("Nenhuma tarefa cadastrada.")
    else:
        print("\nLista de tarefas:")
        for i, tarefa in enumerate(tarefas):
            print(f"{i+1} - {tarefa}")

def remover_tarefa():
    listar_tarefas()
    numero = int(input("Digite o número da tarefa para remover: "))
    if 0 < numero <= len(tarefas):
        tarefas.pop(numero-1)
        print("Tarefa removida!")

def menu():
    while True:

        print("\n===== GERENCIADOR DE TAREFAS =====")
        print("1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Remover tarefa")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_tarefa()

        elif opcao == "2":
            listar_tarefas()

        elif opcao == "3":
            remover_tarefa()

        elif opcao == "0":
            print("Encerrando...")
            break

        else:
            print("Opção inválida!")

menu()

from . import tarefa_service


def mostrar_menu():
    print("=== Gerenciador de Tarefas ===")
    print("1 - Adicionar nova tarefa")
    print("2 - Listar tarefas")
    print("3 - Marcar tarefa como concluída")
    print("4 - Excluir tarefa")
    print("0 - Sair")


def opcao_adicionar():
    print("\n--- Adicionar nova tarefa ---")
    titulo = input("Título: ")
    descricao = input("Descrição: ")
    prioridade = input("Prioridade (baixa/média/alta ou número): ")

    tarefa_service.adicionar_tarefa(titulo, descricao, prioridade)
    print("Tarefa adicionada com sucesso!\n")


def opcao_listar():
    print("\n--- Listar tarefas ---")
    print("1 - Todas")
    print("2 - Filtrar por prioridade")
    print("3 - Filtrar por status")
    escolha = input("Escolha uma opção: ")

    filtro_prioridade = None
    filtro_status = None

    if escolha == "2":
        filtro_prioridade = input("Digite a prioridade para filtrar: ")
    elif escolha == "3":
        print("1 - Somente concluídas")
        print("2 - Somente pendentes")
        tipo = input("Escolha: ")
        if tipo == "1":
            filtro_status = "concluida"
        elif tipo == "2":
            filtro_status = "pendente"

    tarefas = tarefa_service.listar_tarefas(
        filtro_prioridade=filtro_prioridade,
        filtro_status=filtro_status
    )

    if not tarefas:
        print("Nenhuma tarefa encontrada.\n")
        return

    for t in tarefas:
        id_tarefa = t[0]
        titulo = t[1]
        descricao = t[2]
        prioridade = t[3]
        concluida = t[4]
        data_criacao = t[5]

        status = "Concluída" if concluida == 1 else "Pendente"

        print("\n----------------------")
        print(f"ID: {id_tarefa}")
        print(f"Título: {titulo}")
        print(f"Descrição: {descricao}")
        print(f"Prioridade: {prioridade}")
        print(f"Status: {status}")
        print(f"Criada em: {data_criacao}")
    print("")


def opcao_marcar_concluida():
    print("\n--- Marcar tarefa como concluída ---")
    try:
        id_tarefa = int(input("Digite o ID da tarefa: "))
    except ValueError:
        print("ID inválido.\n")
        return

    ok = tarefa_service.marcar_como_concluida(id_tarefa)

    if ok:
        print("Tarefa marcada como concluída!\n")
    else:
        print("Nenhuma tarefa encontrada com esse ID.\n")


def opcao_excluir():
    print("\n--- Excluir tarefa ---")
    try:
        id_tarefa = int(input("Digite o ID da tarefa: "))
    except ValueError:
        print("ID inválido.\n")
        return

    ok = tarefa_service.excluir_tarefa(id_tarefa)

    if ok:
        print("Tarefa excluída com sucesso!\n")
    else:
        print("Nenhuma tarefa encontrada com esse ID.\n")


def loop_principal():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            opcao_adicionar()
        elif opcao == "2":
            opcao_listar()
        elif opcao == "3":
            opcao_marcar_concluida()
        elif opcao == "4":
            opcao_excluir()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida.\n")

from datetime import datetime
from .database import obter_conexao


def adicionar_tarefa(titulo, descricao, prioridade):
    conexao = obter_conexao()
    cursor = conexao.cursor()

    data_criacao = datetime.now().strftime("%Y-%m-%d %H:%M")

    cursor.execute(
        "INSERT INTO tarefas (titulo, descricao, prioridade, concluida, data_criacao) VALUES (?, ?, ?, ?, ?)",
        (titulo, descricao, prioridade, 0, data_criacao)
    )

    conexao.commit()
    conexao.close()


def listar_tarefas(filtro_prioridade=None, filtro_status=None):
    """
    filtro_prioridade: texto ou None
    filtro_status: 'concluida', 'pendente' ou None
    """
    conexao = obter_conexao()
    cursor = conexao.cursor()

    consulta = "SELECT id, titulo, descricao, prioridade, concluida, data_criacao FROM tarefas"
    parametros = []

    condicoes = []

    if filtro_prioridade is not None:
        condicoes.append("prioridade = ?")
        parametros.append(filtro_prioridade)

    if filtro_status == "concluida":
        condicoes.append("concluida = 1")
    elif filtro_status == "pendente":
        condicoes.append("concluida = 0")

    if condicoes:
        consulta += " WHERE " + " AND ".join(condicoes)

    cursor.execute(consulta, parametros)
    tarefas = cursor.fetchall()

    conexao.close()
    return tarefas


def marcar_como_concluida(id_tarefa):
    conexao = obter_conexao()
    cursor = conexao.cursor()

    cursor.execute(
        "UPDATE tarefas SET concluida = 1 WHERE id = ?",
        (id_tarefa,)
    )

    conexao.commit()
    linhas = cursor.rowcount
    conexao.close()
    return linhas > 0


def excluir_tarefa(id_tarefa):
    conexao = obter_conexao()
    cursor = conexao.cursor()

    cursor.execute(
        "DELETE FROM tarefas WHERE id = ?",
        (id_tarefa,)
    )

    conexao.commit()
    linhas = cursor.rowcount
    conexao.close()
    return linhas > 0

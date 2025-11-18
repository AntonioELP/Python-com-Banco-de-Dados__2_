import sqlite3

NOME_BANCO = "tarefas.db"


def obter_conexao():
    # Abre uma conexão com o banco de dados
    conexao = sqlite3.connect(NOME_BANCO)
    return conexao


def criar_tabela():
    conexao = obter_conexao()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descricao TEXT,
            prioridade TEXT,
            concluida INTEGER DEFAULT 0,
            data_criacao TEXT
        )
    """)

    conexao.commit()
    conexao.close()

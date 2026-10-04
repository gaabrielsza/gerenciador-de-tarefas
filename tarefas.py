import sqlite3

def conectar():
    conexao = sqlite3.connect("tarefas.db")
    conexao.execute("""
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao TEXT NOT NULL,
            concluida INTEGER NOT NULL DEFAULT 0
        )
    """)
    return conexao

def adicionar_tarefa(descricao):
    with conectar() as conexao:
        conexao.execute(
            "INSERT INTO tarefas (descricao) VALUES (?)", (descricao,)
        )

if __name__ == "__main__":
    texto = input("Nova tarefa: ")
    adicionar_tarefa(texto)
    print("Tarefa adicionada!")
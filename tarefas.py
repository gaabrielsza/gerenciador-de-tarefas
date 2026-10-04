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

    
def listar_tarefas():
    with conectar() as conexao:
        linhas = conexao.execute(
            "SELECT id, descricao, concluida FROM tarefas"
        ).fetchall()

    if not linhas:
        print("Nenhuma tarefa cadastrada.")
        return

    for id_tarefa, descricao, concluida in linhas:
        if concluida == 1:
            marca = "x"
        else:
            marca = " "
        print(f"[{marca}] {id_tarefa} - {descricao}")


def concluir_tarefa(id_tarefa):
    with conectar() as conexao:
        conexao.execute(
            "UPDATE tarefas SET concluida = 1 WHERE id = ?", (id_tarefa,)
        )

def apagar_tarefa(id_tarefa):
    with conectar() as conexao:
        conexao.execute(
            "DELETE FROM tarefas WHERE id = ?", (id_tarefa,)
        )

if __name__ == "__main__":
    apagar_tarefa(2)
    listar_tarefas()
 
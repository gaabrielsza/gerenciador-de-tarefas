# Gerenciador de Tarefas

Aplicativo de terminal para gerenciar uma lista de tarefas, feito em Python com banco de dados SQLite.

## Funcionalidades

- Adicionar tarefas
- Listar tarefas (pendentes e concluídas)
- Marcar tarefa como concluída
- Apagar tarefa
- Validação de entradas inválidas

## Tecnologias

Python 3 · SQLite (módulo `sqlite3`, já incluído no Python)

## Como executar

    git clone https://github.com/gaabrielsza/gerenciador-de-tarefas.git
    cd gerenciador-de-tarefas
    python tarefas.py

O banco de dados (`tarefas.db`) é criado automaticamente na primeira execução.

## Exemplo de uso

    1 - Adicionar tarefa
    2 - Listar tarefas
    3 - Concluir tarefa
    4 - Apagar tarefa
    0 - Sair
    Escolha: 2
    [x] 1 - Estudar C
    [ ] 2 - Fazer exercícios de Python

## O que pratiquei

CRUD com SQL (`INSERT`, `SELECT`, `UPDATE`, `DELETE`), consultas parametrizadas, funções, laços, tratamento de exceções.

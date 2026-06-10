from fastapi import FastAPI
from tarefas.models import Tarefa
import tarefas.storage as storage


storage.carregar()

app = FastAPI(
    title="API de Tarefas",
    description="API simples para gerenciamento de tarefas",
    version="1.0.0"
)

@app.post("/tarefas")
def adicionar(tarefa: Tarefa):
    nova_tarefa = {
        "id": storage.proximo_id,
        "nome": tarefa.nome,
        "concluida": False
    }

    storage.tarefas.append(nova_tarefa)
    storage.proximo_id += 1
    storage.salvar()

    return nova_tarefa
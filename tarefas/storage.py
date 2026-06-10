import json

ARQUIVO = "tarefas.json"

def carregar():
    try:
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def salvar(tarefas):
    with open(ARQUIVO, "w") as f:
        json.dump(tarefas, f, indent=4)
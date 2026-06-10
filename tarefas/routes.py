from fastapi import APIRouter
from tarefas.models import Tarefa
from tarefas.storage import carregar, salvar

router = APIRouter()

tarefas = carregar()
proximo_id = 1 if not tarefas else max(t["id"] for t in tarefas) + 1


@router.get("/")
def inicio():
    return {"status": "ok"}


@router.post("/tarefas")
def adicionar(tarefa: Tarefa):
    global proximo_id

    nova = {
        "id": proximo_id,
        "nome": tarefa.nome,
        "concluida": False
    }
   

    tarefas.append(nova)
    proximo_id +=1
    salvar(tarefas)

    return nova


@router.get("/tarefas")
def listar(nome=None, concluida=None, limit=3, offset=0):
    resultado = tarefas

    if nome:
        resultado = [t for t in resultado if nome.lower() == t["nome"].lower()]
        
    if concluida is not None:
        resultado = [t for t in resultado if concluida == t["concluida"].lower()]
        
    return {
        "total": len(resultado),
        "limit": limit,
        "offset": offset,
    }
    
@router.put("/tarefas/{id}")
def editar(id: int, dados: Tarefa):
    for t in tarefas:
        if t["id"] == id:
            t["nome"] = dados.nome
            salvar(tarefas)
            return t

    return {"erro": "Não encontrada"}

@router.put("/tarefas/{id}/concluir")
def concluir(id: int):
    for t in tarefas:
        if t["id"] == id:
            t["concluida"] = True
            salvar(tarefas)
            return {"mensagem": "Concluída", "tarefa": t}

    return {"erro": "Não encontrada"}

@router.delete("/tarefas/{id}")
def remover(id: int):
    for i, t in enumerate(tarefas):
        if t["id"] == id:
            tarefa_removida = tarefas.pop(i)
            salvar(tarefas)
            return {
                "mensagem": "Tarefa removida",
                "tarefa": tarefa_removida
            }

    return {"erro": "Tarefa não encontrada"}

@router.get("/tarefas/buscar")
def buscar_por_nome(nome: str):
    resultado = []

    for t in tarefas:
        if nome.lower() in t["nome"].lower():
            resultado.append(t)

    if not resultado:
        return {"mensagem": "Nenhuma tarefa encontrada"}
    return resultado
    
    
        
        
        
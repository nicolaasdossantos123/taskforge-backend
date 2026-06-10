from fastapi import APIRouter
from schemas import Usuario
from sqlalchemy import text
from database import engine
from fastapi import HTTPException

router = APIRouter()

@router.post("/usuarios")
def criar_usuario(usuario: Usuario):
    
    with engine.connect() as conexao:
        
        conexao.execute(
            text(
                """
                INSERT INTO usuarios
                (nome, email, senha)
                VALUES
                (:nome, :email, :senha)
                """
            ),
            {
                "nome": usuario.nome,
                "email": usuario.email,
                "senha": usuario.senha
            }
        )
        conexao.commit()
        
    return {
        "mensagem": "Usuario criado!"
    }
 
@router.get("/usuarios")
def listar_usuarios():

    lista_usuarios = []
    
    with engine.connect() as conexao:
        resultado = conexao.execute(
            text(
                """
                SELECT * FROM usuarios
                """
            ),
            {"id": id}
        )
       
        usuarios = resultado.fetchall()
       
        for usuario in usuarios:
            dados_usuario = {
                "id": usuario[0],
                "nome": usuario[1],
                "email": usuario[2]
            }
               
            lista_usuarios.append(dados_usuario)
        
    return lista_usuarios

@router.get("/usuarios/{id}")
def procurar_usuario(id: int):
    
    with engine.connect() as conexao:
        
        resultado = conexao.execute(
            text(
                """
                SELECT * FROM usuarios
                WHERE id = :id
                """
            ),
        )
        
        usuario = resultado.fetchone()
    
        if usuario is None:
            raise HTTPException(
                status_code=404,
                detail="Usuario não encontrado"
            )
    
    dados_usuario = {
        "id": usuario[0],
        "nome": usuario[1],
        "email": usuario[2]
    }
    
    return dados_usuario

@router.delete("/usuarios/{id}")
def deletar_usuario(id: int):
    
    with engine.connect() as conexao:
        resultado = conexao.execute(
            text(
                """
                SELECT * FROM usuarios
                WHERE id = :id
                """
            ),
            {"id": id}
        )

        usuario_encontrado = resultado.fetchone()
    
        if usuario_encontrado is None:
            raise HTTPException(
                status_code=404,
                detail="Usuário não encontrado"
        )
        
        conexao.execute(
            text(
                """
                DELETE FROM usuarios 
                WHERE id = :id
                """
                
            ),
            {"id": id}
        )
        conexao.commit()
    
    return {
        "mensagem": "Usuário deletado!",
        "id": usuario_encontrado[0],
        "nome": usuario_encontrado[1]
    }

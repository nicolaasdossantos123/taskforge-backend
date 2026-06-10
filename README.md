# TaskForge Backend

API REST para gerenciamento de usuários e tarefas desenvolvida com FastAPI, PostgreSQL e SQLAlchemy.

## Tecnologias

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Uvicorn

## Funcionalidades

### Usuários

- Criar usuário
- Listar usuários
- Buscar usuário por ID
- Deletar usuário

### Tarefas

- Estrutura da tabela criada
- Relacionamento com usuários através de Foreign Key

## Conceitos praticados

- CRUD
- Banco de dados relacional
- Foreign Key
- ON DELETE CASCADE
- SQLAlchemy Core
- Path Parameters
- HTTPException
- fetchone()
- fetchall()

## Estrutura do projeto

```text
taskforge-backend/
│
├── main.py
├── database.py
├── schemas.py
├── routers/
└── README.md
Como executar
Clonar o projeto
git clone https://github.com/nicolaasdossantos123/taskforge-backend.git
Criar ambiente virtual
python -m venv venv
Ativar ambiente virtual

Windows:

venv\Scripts\activate
Instalar dependências
pip install fastapi uvicorn sqlalchemy psycopg2-binary
Executar API
uvicorn main:app --reload
Documentação

Swagger:

http://127.0.0.1:8000/docs
